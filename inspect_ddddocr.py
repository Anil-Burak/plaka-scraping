import ddddocr, inspect
print('Attributes:')
print([a for a in dir(ddddocr.DdddOcr) if not a.startswith('_')])
print('\nDoc:')
print(ddddocr.DdddOcr.__doc__)
# try to print source for a few methods if possible
for name in ['classification','set_model','set_ranges','set_whitelist','set_blacklist']:
    if hasattr(ddddocr.DdddOcr, name):
        print(f"\nMethod {name} found")
        try:
            print(inspect.getsource(getattr(ddddocr.DdddOcr, name)).splitlines()[:40])
        except Exception as e:
            print('Could not get source for', name, e)
    else:
        print(f"\nMethod {name} not found")
