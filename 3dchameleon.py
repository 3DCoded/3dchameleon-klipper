import logging
import time

class Chameleon:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.gcode = self.printer.lookup_object('gcode')
        self.config = config

        self.filament_sensor_name = config.get('filament_sensor_name', 'fsensor')
        self.filament_sensor0 = config.get('filament_sensor0', self.filament_sensor_name)
        self.filament_sensor1 = config.get('filament_sensor1', self.filament_sensor_name)
        self.filament_sensor2 = config.get('filament_sensor2', self.filament_sensor_name)
        self.filament_sensor3 = config.get('filament_sensor3', self.filament_sensor_name)
        self.filament_sensor_type = config.get('filament_sensor_type', 'filament_switch_sensor')
        self.fsensor = self.printer.load_object(self.config, f'{self.filament_sensor_type} {self.filament_sensor_name}')
        self.fsensor0 = self.printer.load_object(self.config, f'{self.filament_sensor_type} {self.filament_sensor0}')
        self.fsensor1 = self.printer.load_object(self.config, f'{self.filament_sensor_type} {self.filament_sensor1}')
        self.fsensor2 = self.printer.load_object(self.config, f'{self.filament_sensor_type} {self.filament_sensor2}')
        self.fsensor3 = self.printer.load_object(self.config, f'{self.filament_sensor_type} {self.filament_sensor3}')

        self.pin = config.get('pin', '3dchameleon')
        self.chameleon_pin = self.printer.load_object(self.config, f'output_pin {self.pin}')

        self.unload_time = config.getfloat('unload_time', 7.5)
        self.max_unload_time = config.getfloat('max_unload_time', 10)
        self.load_time = config.getint('load_time', 0.5)
        self.max_load_time = config.getfloat('max_load_time', self.load_time + 10)
        self.pulse_time = config.getfloat('pulse_time', 0.5)

        self.filament_detected = [False] * 5

        logging.info('3DChameleon: Initialized Successfully')

        self.gcode.register_command(
            'UPDATE_CHAMELEON_SENSOR',
            self.cmd_UPDATE_CHAMELEON_SENSOR
        )

        self.gcode.register_command(
            'SET_CHAMELEON',
            self.cmd_SET_CHAMELEON,
            self.cmd_SET_CHAMELEON_help
        )

        self.gcode.register_command(
            'UNLOAD_CHAMELEON',
            self.cmd_UNLOAD_CHAMELEON,
            self.cmd_UNLOAD_CHAMELEON_help
        )

        self.gcode.register_command(
            'LOAD_CHAMELEON',
            self.cmd_LOAD_CHAMELEON,
            self.cmd_LOAD_CHAMELEON_help
        )

        self.gcode.register_command(
            'PRESS_CHAMELEON',
            self.cmd_PRESS_CHAMELEON,
            self.cmd_PRESS_CHAMELEON_help
        )

        self.gcode.register_command(
            'PULSE_CHAMELEON',
            self.cmd_PULSE_CHAMELEON,
            self.cmd_PULSE_CHAMELEON_help
        )

        self.gcode.register_command(
            'QUERY_CHAMELEON_SENSOR',
            self.cmd_QUERY_CHAMELEON_SENSOR,
            self.cmd_QUERY_CHAMELEON_SENSOR_help
        )

        self.printer.register_event_handler("klippy:ready", lambda: self.cmd_UPDATE_CHAMELEON_SENSOR(None))
    
    def _read_fsensor(self):
        return [self.fsensor0.runout_helper.filament_present, self.fsensor1.runout_helper.filament_present, self.fsensor2.runout_helper.filament_present, self.fsensor3.runout_helper.filament_present, self.fsensor.runout_helper.filament_present]
    
    def _set_chameleon(self, value):
        toolhead = self.printer.lookup_object('toolhead')
        toolhead.register_lookahead_callback(
            lambda print_time: self.chameleon_pin._set_pin(print_time, value))
    
    def cmd_UPDATE_CHAMELEON_SENSOR(self, gcmd=None):
        self.filament_detected = self._read_fsensor()
    
    cmd_UNLOAD_CHAMELEON_help = 'Unloads the 3DChameleon until the filament is past the filament runout sensor (when it reads False), and then waits unload_time to pull the filament out of the way for the next filament. Note that if the filament takes more than max_unload_time to trigger the filament sensor, then it will abort'
    def cmd_UNLOAD_CHAMELEON(self, gcmd):
        tool = gcmd.get_int('TOOL')
        self._set_chameleon(True)
        start = time.time()
        self.gcode.run_script_from_command('UPDATE_CHAMELEON_SENSOR')
        while self.filament_detected[tool]:
            logging.info(f'3DChameleon Unload Sensor: {self.filament_detected[tool]}')
            self.gcode.run_script_from_command('UPDATE_CHAMELEON_SENSOR')
            if time.time() - start > self.max_unload_time:
                self._set_chameleon(False)
                self.gcode.run_script_from_command('M117 Unload Failed')
                self.gcode.run_script_from_command('PAUSE')
                break
            self.gcode.run_script_from_command('G4 P250')
        self.gcode.run_script_from_command(f'G4 P{self.unload_time * 1000}')
        self._set_chameleon(False)
    
    cmd_LOAD_CHAMELEON_help = 'Loads the 3DChameleon until the filament is past the filament runout sensor (when it reads True), and then waits load_time to push the filament into the extruder. Note that if the filament takes more than max_load_time to trigger the filament sensor, then it will abort'
    def cmd_LOAD_CHAMELEON(self, gcmd):
        self._set_chameleon(True)
        start = time.time()
        self.gcode.run_script_from_command('UPDATE_CHAMELEON_SENSOR')
        while not self.filament_detected:
            logging.info(f'3DChameleon Load Sensor: {self.filament_detected}')
            self.gcode.run_script_from_command('UPDATE_CHAMELEON_SENSOR')
            if time.time() - start > self.max_load_time:
                self._set_chameleon(False)
                self.gcode.run_script_from_command('M117 Load Failed')
                self.gcode.run_script_from_command('PAUSE')
                break
            self.gcode.run_script_from_command('G4 P250')
        self.gcode.run_script_from_command(f'G4 P{self.load_time * 1000}')
        self._set_chameleon(False)
    
    cmd_PULSE_CHAMELEON_help = 'Presses the 3DChameleon for the duration of PULSES * pulse_time'
    def cmd_PULSE_CHAMELEON(self, gcmd):
        self._set_chameleon(True)
        pulses = gcmd.get_int('PULSES', 0)
        pulses_ms = int(pulses * self.pulse_time * 1000)
        self.gcode.run_script_from_command(f'G4 P{pulses_ms}')
        self._set_chameleon(False)
    
    cmd_PRESS_CHAMELEON_help = 'Press the 3DChameleon for the duration of DURATION'
    def cmd_PRESS_CHAMELEON(self, gcmd):
        self._set_chameleon(True)
        duration = gcmd.get_float('DURATION', 0)
        duration_ms = int(duration * 1000)
        self.gcode.run_script_from_command(f'G4 P{duration_ms}')
        self._set_chameleon(False)
    
    cmd_SET_CHAMELEON_help = 'Sets the 3DChameleon pin to HIGH or LOW, as determined by VALUE'
    def cmd_SET_CHAMELEON(self, gcmd):
        value = gcmd.get_int('VALUE', 0)
        self._set_chameleon(value)
        gcmd.respond_info(f'Set 3DChameleon = {value}')
    
    cmd_QUERY_CHAMELEON_SENSOR_help = 'Returns the current state of the 3DChameleon filament sensor'
    def cmd_QUERY_CHAMELEON_SENSOR(self, gcmd):
        value = self._read_fsensor()
        gcmd.respond_info(f'Sensor value: {value}')

def load_config(config):
    return Chameleon(config)