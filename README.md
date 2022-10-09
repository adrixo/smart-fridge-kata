

- Track items placed into and out of the fridge
- When an item is added, record:
    - Item name
    - Expiration date
    - Timestamp when added
- When fridge is opened items are degraded:
    - opened: 1h
    - unopene: 5h
- Add formated display to view contents in this order:
    - any items past their expiry must be displayed first
    - the rest are displayed by expring date
- An item is expired when the tracked expiry reaches midnight on the day after expiration date
- Simulate days passed, so the funcionality can be easily demonstrated
