# Homework 16: Smart Home Inventory (Iterator Pattern)

Implement the **Iterator Design Pattern** to manage a collection of smart home devices.

## Learning Goals

- Understand the Iterator Pattern structure (Aggregate and Iterator)
- Implement `__iter__()` and `__next__()` in Python
- Learn how to make a custom collection iterable

## Requirements

### Class: `Device` (Provided)
A simple class representing a smart device.
- `name`: string (e.g., "Living Room Light")
- `type`: string (e.g., "Light", "Thermostat", "Camera")

### Class: `SmartHome` (Aggregate)
A collection that holds multiple devices.
- `__init__()`: Initialize an empty list of devices.
- `add_device(device)`: Add a `Device` object to the collection.
- `__iter__()`: Should return an instance of `SmartHomeIterator`.

### Class: `SmartHomeIterator` (Iterator)
The custom iterator for `SmartHome`.
- `SmartHomeIterator(devices)`: Use the device list from `SmartHome`.
- `__next__()`: Returns the next device. Raises `StopIteration` at the end.

## Access Level Summary

| Attribute/Method | Type | Access |
|-----------------|------|--------|
| `name`, `device_type` | Instance | Public (Device) |
| `devices` | Instance | Public (SmartHome) |
| `_devices`, `_index` | Instance | Protected (Iterator) |
| `__iter__()` | Method | Public Protocol |
| `__next__()` | Method | Public Protocol |

## Expected Output

When running `chk_homework.py`, you should see:

```
=== Testing SmartHome Iterator ===
PASS: Created SmartHome with 3 devices
PASS: Successfully iterated through all devices
PASS: Iterator raised StopIteration at the end

=== Testing Multiple Iterators ===
PASS: Two independent iterators working correctly

=== All Tests Passed ===
```

## Testing

Run `chk_homework.py` to verify your implementation.

## Submission

Submit `homework.py` via GitHub Classroom.
