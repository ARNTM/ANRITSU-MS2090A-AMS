import sys

def flags():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    if '-help' in opts:
        print(f'Welcome to ANRITSU MS2090A Automatic Measurement System.\n\nHere you can find the parameters that you can use\n -f config_file : This parameter allows you to load a configuration file.\n --skipSetup : This parameter allows you to skip the setup process. It requires the use of -f argument\n\n')
        sys.exit(0)