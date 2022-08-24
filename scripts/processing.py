import argparse
import mymodule.mycode as sk
import logging

def initialize():
    parser = argparse.ArgumentParser(description='MySoftware')
    parser.add_argument('--epochs', type=int, nargs='?', help='Int, >0, Epochs')
    parser.add_argument('--imageroot', type=str, nargs='?', help='Directory containing images')
    args = parser.parse_args()
    configuration = {'epochs':20, 'imageroot':'.'}
    for k in configuration:
        try:
            argk = getattr(args, k)
            if argk is not None:
                configuration[k] = argk
        except AttributeError as e:
            continue
    return configuration


if __name__ == "__main__":
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(format=FORMAT)
    lgr = logging.getLogger('global')
    lgr.setLevel(logging.INFO)
    config = initialize()
    lgr.info("Starting with config P{}".format(config))
    lgr.info("{}".format(sk.myfunction([2])))
    ### for image in images
    ###     curate(image)
