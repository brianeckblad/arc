# Python Coding Standards — Examples

Quick rules: no `str(e)` in JSON responses, all imports at module level, initialize before `try`, use Pythonic style (PEP 8/257), prefer named callables over `lambda`, type hints on public functions, format with `black`/`isort`, catch specific exceptions, no side effects at import, no global mutable state, use context managers, fail fast/raise early, functions do one thing, meaningful names, prefer built-ins/stdlib, prefer comprehensions, pin dependencies, use virtual environments.

## Error Handling — Never str(e) in JSON

```python
# BAD
try:
    result = do_something()
except Exception as e:
    return jsonify({'error': str(e)}), 500

# GOOD
try:
    result = do_something()
except Exception as e:
    logger.exception("operation failed")
    return jsonify({'error': safe_error_message(e)}), 500
```

## Imports — Always at Module Level

```python
# BAD
def handler():
    from some.module import something  # ❌ deferred import without justification
    
# GOOD
from some.module import something  # ✓ at module level

# ALLOWED (with comment)
def handler():
    from circular.module import thing  # Deferred: avoids circular import
```

## Variable Initialization — Before try Block

```python
# BAD
try:
    conn = connect()
    result = conn.query()
finally:
    conn.close()  # NameError if connect() failed

# GOOD
conn = None
try:
    conn = connect()
    result = conn.query()
finally:
    if conn:
        conn.close()
```

## Context Managers — Always Use with

```python
# BAD
f = open('file.txt')
data = f.read()
f.close()

# GOOD
with open('file.txt') as f:
    data = f.read()
```

## Function Size — Keep Focused

```python
# BAD — doing too much
def process_user_request(request):
    # validate (10 lines)
    # authenticate (15 lines)
    # query database (20 lines)
    # transform results (25 lines)
    # log and return (10 lines)
    
# GOOD — extract helpers
def process_user_request(request):
    user = validate_and_authenticate(request)
    data = fetch_user_data(user.id)
    return format_response(data)
```

## Comprehensions — Prefer When Readable

```python
# BAD
result = []
for item in items:
    if item.active:
        result.append(item.name.upper())

# GOOD
result = [item.name.upper() for item in items if item.active]
```
