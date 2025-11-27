import React, { createContext, useContext, useState, ReactNode } from 'react';
import orgData from '../data/struktur';
import type { Member } from '../data/struktur';

interface OrgContextProps {
  members: Member[];
  setMembers: React.Dispatch<React.SetStateAction<Member[]>>;
}

const OrgContext = createContext<OrgContextProps | undefined>(undefined);

export const OrgProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [members, setMembers] = useState<Member[]>(orgData);
  return (
    <OrgContext.Provider value={{ members, setMembers }}>
      {children}
    </OrgContext.Provider>
  );
};

export const useOrg = () => {
  const context = useContext(OrgContext);
  if (!context) throw new Error('useOrg must be used within OrgProvider');
  return context;
};
