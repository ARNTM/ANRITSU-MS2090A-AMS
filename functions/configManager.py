import sys
import os
import json

def saveConfig(config, config_file):
    with open(config_file, "w") as f:
        json.dump(config, f)

def loadConfig(opts, args):
    c = {}
    if "-f" in opts:
        config_file = f"config_files/{args[0]}.json"
    else:
        config_file = "config_files/anritsu_config.json"

    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = json.load(f)
            c['IP_from_config'] = config['IP']
            c['PORT_from_config'] = config['PORT']
            c['CENTRAL_FREQ_from_config'] = config['CENTRAL_FREQ']
            c['FREQ_UNITS_from_config'] = config['FREQ_UNITS']
            c['SPAN_from_config'] = config['SPAN']
            c['SPAN_UNITS_from_config'] = config['SPAN_UNITS']
            c['SWEEP_POINTS_from_config'] = config['SWEEP_POINTS']
            c['INTEGRATION_BANDWIDTH_from_config'] = config['INTEGRATION_BANDWIDTH']
            c['INTEGRATION_BANDWIDTH_UNITS_from_config'] = config['INTEGRATION_BANDWIDTH_UNITS']
            c['SWEEP_TIME_from_config'] = config['SWEEP_TIME']
            c['SWEEP_CONTINUOUSLY_from_config'] = config['SWEEP_CONTINUOUSLY']
            c['PRE_AMP_from_config'] = config['PRE_AMP']
        return [c, config_file]
    else:
        config = {}
        config['IP'] = "192.168.0.11"
        config['PORT'] = "9001"
        config['CENTRAL_FREQ'] = "855"
        config['FREQ_UNITS'] = "MHz"
        config['SPAN'] = "1"
        config['SPAN_UNITS'] = "MHz"
        config['SWEEP_POINTS'] = "10001"
        config['INTEGRATION_BANDWIDTH'] = "250"
        config['INTEGRATION_BANDWIDTH_UNITS'] = "kHz"
        config['SWEEP_TIME'] = "0.1"
        config['SWEEP_CONTINUOUSLY'] = "yes"
        config['PRE_AMP'] = "yes"
        c['IP_from_config'] = config['IP']
        c['PORT_from_config'] = config['PORT']
        c['CENTRAL_FREQ_from_config'] = config['CENTRAL_FREQ']
        c['FREQ_UNITS_from_config'] = config['FREQ_UNITS']
        c['SPAN_from_config'] = config['SPAN']
        c['SPAN_UNITS_from_config'] = config['SPAN_UNITS']
        c['SWEEP_POINTS_from_config'] = config['SWEEP_POINTS']
        c['INTEGRATION_BANDWIDTH_from_config'] = config['INTEGRATION_BANDWIDTH']
        c['INTEGRATION_BANDWIDTH_UNITS_from_config'] = config['INTEGRATION_BANDWIDTH_UNITS']
        c['SWEEP_TIME_from_config'] = config['SWEEP_TIME']
        c['SWEEP_CONTINUOUSLY_from_config'] = config['SWEEP_CONTINUOUSLY']
        c['PRE_AMP_from_config'] = config['PRE_AMP']
        os.makedirs("config_files", exist_ok=True)
        with open(config_file, "w") as f:
            json.dump(config, f)
        return [c, config_file]