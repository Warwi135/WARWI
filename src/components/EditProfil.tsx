import { useState } from "react";
import "./ModalEdit.css";

interface EditProfilProps {
  data: {
    id: number;
    name: string;
    position?: string;
    role?: string;
    level?: number;
    parent_id?: number | null;
    photo?: string;
  };
  onClose: () => void;
  onSubmit: (formData: FormData) => void; // ✅ wajib ada
}

export default function EditProfil({ data, onClose, onSubmit }: EditProfilProps) {
  const [name, setName] = useState(data.name || "");
  const [position, setPosition] = useState(data.position || "");
  const [role, setRole] = useState(data.role || "");
  const [level, setLevel] = useState<string>(data.level ? String(data.level) : "1");
  const [parentId, setParentId] = useState<number | null>(data.parent_id ?? null);
  const [photo, setPhoto] = useState<File | null>(null);
  
  const handleSubmit = () => {
    const formData = new FormData();
    formData.append("name", name.trim());
    formData.append("position", position.trim());
    formData.append("role", role.trim());
    formData.append("level", level || "1");
    formData.append("parent_id", parentId !== null ? String(parentId) : "");

    // Photo wajib ada di FormData
    if (photo) {
      formData.append("photo", photo); // file baru
    } else if (data.photo) {
      formData.append("photo", data.photo); // edit: tetap kirim nama file lama
    } else {
      formData.append("photo", ""); // tambah baru tapi kosong
    }

    onSubmit(formData); // panggil dari parent (ProfilAdmin.tsx)
  };

  return (
    <div className="modal-overlay">
      <div className="modal-box">
        <h2>{data.id === 0 ? "Tambah Anggota Baru" : "Edit Anggota"}</h2>

        <label>Nama</label>
        <input value={name} onChange={(e) => setName(e.target.value)} />

        <label>Jabatan</label>
        <input value={position} onChange={(e) => setPosition(e.target.value)} />

        <label>Role</label>
        <select value={role} onChange={(e) => setRole(e.target.value)}>
          <option value="">-- Pilih Role --</option>
          <option value="lurah">Lurah</option>
          <option value="sekretaris">Sekretaris</option>
          <option value="bendahara">Bendahara</option>
          <option value="pengurus">Pengurus Barang</option>
          <option value="kasatpel">Kasatpel Dukcapil</option>
          <option value="puskesmas">Puskesmas</option>
          <option value="plkb">PLKB</option>
          <option value="gulkarmat">Gulkarmat</option>
          <option value="satpolpp">SatpolPP</option>
          <option value="ptsp">PTSP</option>
          <option value="kesra">Kasi Kesejahteraan</option>
          <option value="pemerintahan">Kasi Pemerintahan</option>
          <option value="ekonomi">Kasi Ekonomi</option>
          <option value="staf">Staf</option>
        </select>

        <label>Level</label>
        <input
          type="number"
          min={1}
          value={level}
          onChange={(e) => setLevel(e.target.value)}
        />

        <label>Foto</label>
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setPhoto(e.target.files?.[0] || null)}
        />

        <div className="modal-actions">
          <button onClick={handleSubmit} className="btn-save">Simpan</button>
          <button onClick={onClose} className="btn-cancel">Batal</button>
        </div>
      </div>
    </div>
  );
}
