import json
import argparse


def log_parser(cmdline=None):
    parser = argparse.ArgumentParser(description='My example explanation')
    parser.add_argument('--log-file', help='specify the path to the log file', required=True)
    if cmdline is not None:
        args = parser.parse_args(cmdline.split())
    else:
        args = parser.parse_args()
    filepath = args.log_file

    with open(filepath, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            log_line = line.split(' ', 3)

            log_timestamp = log_line[0]
            log_stream = log_line[1]

            log_body = json.loads(log_line[3])
            log_level = '[' + log_body['level'] + ']'
            log_message = log_body['message']

            log_template ={ 
              "@timestamp": log_timestamp, 
              "stream": log_stream, 
              "log": log_level + " " + log_message
            }
            #json_output = json.dumps(log_template) 
            json_output = json.dumps(log_template, indent = 4) 
            print(json_output)
    return json_output
            


if __name__ == "__main__":
    log_parser()
