# JavaScript Coding Standards — Examples

## Modal / Pending-State Lifecycle

Confirm flows that mutate pending state must follow a strict single-owner pattern. The **confirm function** owns the full lifecycle: snapshot → execute → clean up. Executors never read or reset `pending*` / `bulk*` state directly.

```javascript
// GOOD — single owner, try/finally guarantees cleanup even on error
async function confirmDelete() {
    const sku = pendingAction.sku;   // 1. Snapshot state before any async work
    try:
        await executeDelete(sku);    // executor takes values as args
    } finally {
        pendingAction = { type: null, sku: null };  // always runs
    }
}

// Cancel path clears immediately — no async, no try/finally needed
function cancelDelete() {
    pendingAction = { type: null, sku: null };
    closeModal();
}

// Executor accepts values as parameters — never reads/resets global state
async function executeDelete(sku) { ... }
```

## Declare Related State Variables Together

All variables that form a single logical state group must be declared in one contiguous block at the top of their scope. Do not scatter or redeclare.

```javascript
// GOOD — all related state in one block
let currentAction   = null;
let selectedItems   = [];
let scheduleDays    = 0;
```

## Use Registry Arrays for Grouped DOM Operations

When multiple modals (or other elements) must be hidden/reset together, define a constant array of their IDs and iterate — do not duplicate calls across functions.

```javascript
const MODAL_IDS = ['confirmModal', 'selectionModal', 'actionModal'];

function closeAllModals() {
    MODAL_IDS.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = 'none';
    });
}
```
