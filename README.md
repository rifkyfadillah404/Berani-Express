# Courier Core - Incident Log System

Odoo 18.0 module untuk manajemen insiden internal BeraniExpress.

## Fitur

- **Data Model**: `courier.incident` dengan field lengkap (judul, pelanggan, resi, tipe, waktu, urgensi, kronologi, catatan, status)
- **State Workflow**: Draft → Follow-up → Done
- **UI/UX**: Tree view dengan decorations, Form view dengan status bar dan chatter
- **Validasi**: SQL constraint untuk mencegah duplikasi, Python constraint untuk memastikan catatan diisi

## Instalasi

1. Copy folder `courier_core` ke Odoo addons path
2. Restart Odoo server
3. Update Apps List: Settings → Apps → Update Apps List
4. Install module "Courier Core - Incident Log System"

## Testing Manual

### 1. Create Incident
- Buka menu **Courier** → **Log Insiden**
- Klik **New**
- Isi data:
  - Judul Insiden: "Paket Rusak"
  - Pelanggan: (pilih atau buat baru)
  - Tipe: Delay / Lost Item / Health / Other
  - Urgensi: Low / Medium / High
  - Kronologi: (opsional)
- Klik **Save**
- Status: **Draft**

### 2. Mark Follow-up
- Klik tombol **Mark Follow-up**
- Status berubah menjadi: **Follow Up**
- Row di tree view berwarna kuning (warning)

### 3. Resolve
- Isi **Catatan Follow-up** (wajib!)
- Klik tombol **Resolve**
- Status berubah menjadi: **Done**
- Field `Selesai pada` terisi otomatis
- Row di tree view berwarna hijau (success)

## Struktur Module

```
courier_core/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── courier_incident.py
├── views/
│   └── courier_incident_views.xml
├── security/
│   └── ir.model.access.csv
└── README.md
```

## Technical Specifications

- **SQL Constraints**: Unique combination of `customer_id + incident_type + incident_datetime`
- **Python Constraints**: `followup_note` required when state is 'done'
- **Tree Decorations**: Warning (yellow) for 'followup', Success (green) for 'done'
