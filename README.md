# Courier Core - Incident Log System

Odoo 18.0 module untuk manajemen insiden internal BeraniExpress.

## Fitur

### 1. Model Data (`courier.incident`)

| Field | Label | Tipe Data | Ketentuan |
|-------|-------|-----------|-----------|
| `name` | Judul Insiden | Char | Required |
| `customer_id` | Pelanggan | Many2one | Relasi ke `courier.customer` (Required) |
| `shipment_id` | No. Resi | Many2one | Relasi ke `courier.shipment` |
| `incident_type` | Tipe | Selection | 'health', 'lost_item', 'delay', 'other' (Default: 'other') |
| `incident_datetime` | Waktu | Datetime | Required, default: sekarang |
| `severity` | Urgensi | Selection | 'low', 'medium', 'high' (Default: 'low') |
| `description` | Kronologi | Text | Detail kejadian |
| `followup_note` | Catatan | Text | Tindakan yang diambil |
| `state` | Status | Selection | 'draft', 'followup', 'done' (Default: 'draft') |
| `resolved_at` | Selesai pada | Datetime | Read only, terisi otomatis saat Done |

### 2. Antarmuka Pengguna (UI/UX)

- **Tree View**: Daftar insiden dengan status, decorations warning/success
- **Form View**: Status bar, sheet dengan 2 kolom, notebook untuk kronologi/catatan, chatter
- **Menu**: Courier → Log Insiden

### 3. Logika Bisnis (State Workflow)

- **Mark Follow-up**: Mengubah state menjadi 'followup'
- **Resolve**: Mengubah state menjadi 'done' dan mengisi `resolved_at`

### 4. Tantangan Tambahan

- **SQL Constraints**: Mencegah duplikasi `customer_id` + `incident_type` + `incident_datetime`
- **UI Decorations**: `decoration-warning` untuk 'followup', `decoration-success` untuk 'done'
- **Python Validation**: `@api.constrains` memastikan `followup_note` wajib diisi saat status 'done'

## Instalasi

1. Copy folder `courier_core` ke Odoo addons path
2. Restart Odoo server
3. Update Apps List: Settings → Apps → Update Apps List
4. Install module "Courier Core - Incident Log System"

## Testing Manual

### 1. Create Incident
- Buka menu **Courier** → **Log Insiden**
- Klik **New**
- Isi data: Judul Insiden, Pelanggan, Tipe, Urgensi
- Klik **Save**
- Status: **Draft**

### 2. Mark Follow-up
- Klik tombol **Mark Follow-up**
- Status berubah menjadi: **Follow Up**
- Row di tree view berwarna kuning (warning)

### 3. Resolve
- Isi **Catatan** (wajib!)
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
