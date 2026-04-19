import h5py
import json

def inspect_model(model_path):
    print(f"Inspeccionando {model_path}...")
    try:
        with h5py.File(model_path, mode='r') as f:
            if 'model_config' not in f.attrs:
                print("Error: No se encontró 'model_config'.")
                return
            
            config_str = f.attrs.get('model_config')
            if isinstance(config_str, bytes):
                config_str = config_str.decode('utf-8')
            
            config = json.loads(config_str)
            print("Estructura base:", config.keys())
            if 'config' in config:
                print("Config keys:", config['config'].keys())
                if 'layers' in config['config']:
                    print(f"Número de capas: {len(config['config']['layers'])}")
                    for i, layer in enumerate(config['config']['layers']):
                        if layer['class_name'] == 'DepthwiseConv2D':
                            print(f"Capa {i} (DepthwiseConv2D): {layer['config'].keys()}")
                            if 'groups' in layer['config']:
                                print("  -> TIENE 'groups'")
                            else:
                                print("  -> NO tiene 'groups'")
                        elif 'layers' in layer['config']: # Nested model?
                             print(f"Capa {i} ({layer['class_name']}) tiene subcapas?")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_model("keras_model.h5")
