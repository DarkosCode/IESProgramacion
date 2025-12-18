import h5py
import json

def clean_layer_config(layer_config):
    """
    Recursively remove 'groups' from DepthwiseConv2D config.
    Returns True if any change was made.
    """
    changed = False
    
    # Check current layer
    if layer_config.get('class_name') == 'DepthwiseConv2D':
        if 'config' in layer_config and 'groups' in layer_config['config']:
            print(f"Eliminando 'groups' de {layer_config['config'].get('name', 'unknown layer')}")
            del layer_config['config']['groups']
            changed = True
    
    # Check nested layers (for Sequential or Functional models)
    if 'config' in layer_config:
        # Sequential models store layers in config['layers']
        if 'layers' in layer_config['config']:
             for layer in layer_config['config']['layers']:
                 if clean_layer_config(layer):
                     changed = True
        
        # Some other structures might need inspection, but this covers 99% of cases
    
    return changed

def patch_model(model_path):
    print(f"Abriendo {model_path} para parchar recursivamente...")
    try:
        with h5py.File(model_path, mode='r+') as f:
            if 'model_config' not in f.attrs:
                print("Error: No se encontró 'model_config'.")
                return False
            
            config_str = f.attrs.get('model_config')
            if isinstance(config_str, bytes):
                config_str = config_str.decode('utf-8')
            
            config = json.loads(config_str)
            
            # Start recursion from result config
            # config is usually {'class_name': 'Sequential', 'config': {'layers': [...]}}
            
            updated = False
            # Can treat the top level config as a layer config effectively
            updated = clean_layer_config(config)
            
            if updated:
                new_config_str = json.dumps(config)
                f.attrs['model_config'] = new_config_str
                print("¡Archivo parchado exitosamente!")
                return True
            else:
                print("No se encontraron capas para arreglar (recursivo).")
                return True
                
    except Exception as e:
        print(f"Error al parchar: {e}")
        return False

if __name__ == "__main__":
    if patch_model("keras_model.h5"):
        print("Parche terminado.")
