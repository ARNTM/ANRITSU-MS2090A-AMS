import sys
import os
import json

def setup(opts, optsWOArgs, args):
    config, file = loadConfig(opts, args)
    unitsAvailable = ['Hz', 'kHz', 'MHz', 'GHz']
    yesno = ['yes', 'no']
    unitsStr = ', '.join([str(elem) for elem in unitsAvailable])
    freqUnits = ''
    spanUnits = ''
    integrationBandwidthUnits = ''
    sweepContinuously = ''
    preAmp = ''
    if ('--skipSetup' in optsWOArgs and '-f' in opts):
        print("\n\n[✓] Skipping setup...")
        ip = config['IP_from_config']
        port = config['PORT_from_config']
        centralFreq = config['CENTRAL_FREQ_from_config']
        freqUnits = config['FREQ_UNITS_from_config']
        span = config['SPAN_from_config']
        spanUnits = config['SPAN_UNITS_from_config']
        sweepPoints = config['SWEEP_POINTS_from_config']
        integrationBandwidth = config['INTEGRATION_BANDWIDTH_from_config']
        integrationBandwidthUnits = config['INTEGRATION_BANDWIDTH_UNITS_from_config']
        sweepTime = config['SWEEP_TIME_from_config']
        sweepContinuously = config['SWEEP_CONTINUOUSLY_from_config']
        preAmp = config['PRE_AMP_from_config']
    else:
        ip = str(input(f"Enter IP address [{config['IP_from_config']}]: ") or config['IP_from_config'])
        port = str(input(f"Enter port number [{config['PORT_from_config']}]: ") or config['PORT_from_config'])
        centralFreq = str(input(f"Enter central frequency [{config['CENTRAL_FREQ_from_config']}]: ") or config['CENTRAL_FREQ_from_config'])
        while freqUnits not in unitsAvailable:
            freqUnits = str(input(f"Enter frequency units ({unitsStr}) [{config['FREQ_UNITS_from_config']}]: ") or config['FREQ_UNITS_from_config'])
        span = str(input(f"Enter span [{config['SPAN_from_config']}]: ") or config['SPAN_from_config'])
        while spanUnits not in unitsAvailable:
            spanUnits = str(input(f"Enter frequency units ({unitsStr}) [{config['SPAN_UNITS_from_config']}]: ") or config['SPAN_UNITS_from_config'])
        sweepPoints = str(input(f"Enter number of sweep points [{config['SWEEP_POINTS_from_config']}]: ") or config['SWEEP_POINTS_from_config'])
        integrationBandwidth = str(input(f"Enter integration bandwidth [{config['INTEGRATION_BANDWIDTH_from_config']}]: ") or config['INTEGRATION_BANDWIDTH_from_config'])
        while integrationBandwidthUnits not in unitsAvailable:
            integrationBandwidthUnits = str(input(f"Enter integration bandwidth units ({unitsStr}) [{config['INTEGRATION_BANDWIDTH_UNITS_from_config']}]: ") or config['INTEGRATION_BANDWIDTH_UNITS_from_config'])
        sweepTime = str(input(f"Enter sweep time [{config['SWEEP_TIME_from_config']}]: ") or config['SWEEP_TIME_from_config'])
        while sweepContinuously not in yesno:
            sweepContinuously = str(input(f"Sweep continuously? [{config['SWEEP_CONTINUOUSLY_from_config']}]: ") or config['SWEEP_CONTINUOUSLY_from_config'])
        while preAmp not in yesno:
            preAmp = str(input(f"Enable pre-amp? [{config['PRE_AMP_from_config']}]: ") or config['PRE_AMP_from_config'])
    return [ip, port, centralFreq, freqUnits, span, spanUnits, sweepPoints, integrationBandwidth, integrationBandwidthUnits, sweepTime, sweepContinuously, preAmp, file]


def saveConfig(ip,port,centralFreq,freqUnits, span, spanUnits, sweepPoints, integrationBandwidth, integrationBandwidthUnits, sweepTime,sweepContinuously,preAmp,config_file):
    config = {}
    config['IP'] = ip
    config['PORT'] = port
    config['CENTRAL_FREQ'] = centralFreq
    config['FREQ_UNITS'] = freqUnits
    config['SPAN'] = span
    config['SPAN_UNITS'] = spanUnits
    config['SWEEP_POINTS'] = sweepPoints
    config['INTEGRATION_BANDWIDTH'] = integrationBandwidth
    config['INTEGRATION_BANDWIDTH_UNITS'] = integrationBandwidthUnits
    config['SWEEP_TIME'] = sweepTime
    config['SWEEP_CONTINUOUSLY'] = sweepContinuously
    config['PRE_AMP'] = preAmp
    with open(config_file, "w") as f:
        json.dump(config, f)

def loadConfig(opts, args):
    c = {}
    if "-f" in opts:
        config_file = f"config_files/{args[0]}.json"
    else:
        config_file = "config_files/anritsu_config.json"

    if os.path.exists('data/'):
        pass
    else:
        os.mkdir('data/')
        
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