
def to_json(**kwargs):
  """Convert object to json"""
  result = {}

  for key, value in kwargs.items():
    if not key.startswith('_sa_instance_state'):
      result[key] = value
    
  return result
