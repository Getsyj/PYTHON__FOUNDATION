import os

def read_db_config(file_name='resources/db.properties'):
    config = {}

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, file_name)

    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()

    return config
if __name__ == "__main__":
    config = read_db_config()
    print(config)
