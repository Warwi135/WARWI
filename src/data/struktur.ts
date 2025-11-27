export interface Member {
  id: number;
  name: string;
  position: string;
  photo: string;
  parentId: number | null;
  x: number;
  y: number;
  branch?: string;
}

const orgData: Member[] = [
  { id: 1, name: "", position: "AGUS SULAEMAN \nKELURAHAN CAKUNG BARAT", photo: "", parentId: null, x: 600, y: 30 },
  { id: 2, name: "", position: "HARIYANTI \nKELURAHAN CAKUNG BARAT", photo: "", parentId: 1, x: 1050, y: 180, branch: "right" },
  { id: 3, name: "", position: "SESTIA Akbarani \nBENDAHARA", photo: "", parentId: 2, x: 920, y: 380 },
  { id: 4, name: "", position: "ROSEMILLAH LASE \nPENGURUS BARANG", photo: "", parentId: 2, x: 1180, y: 380 },
  { id: 5, name: "", position: "RICKI SUGIARTO \nKASI PEMERINTAHAN", photo: "", parentId: 1, x: 80, y: 380, branch: "left" },
  { id: 6, name: "", position: "KASI EKONOMI\nPEMBANGUNAN", photo: "", parentId: 1, x: 370, y: 380, branch: "middle" },
  { id: 7, name: "", position: "TRI HASTUTI \nKASI KESEJAHTERAAN\nRAKYAT", photo: "", parentId: 1, x: 660, y: 380, branch: "middle" },
  { id: 8, name: "", position: "MUFTI ASHARI \nSTAF PEMERINTAHAN", photo: "", parentId: 5, x: 80, y: 600 },
  { id: 9, name: "", position: "INDRA SUKACA \nSTAF EKONOMI PEMBANGUNAN", photo: "", parentId: 6, x: 370, y: 600 },
  { id: 10, name: "", position: "ANTTONIUS KHARISMA \nSTAF KESEJAHTERAAN RAKYAT", photo: "", parentId: 7, x: 660, y: 600 }
];

export default orgData;