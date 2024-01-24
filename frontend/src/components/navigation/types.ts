export type NavLinkLeaf = { name: string; href: string; type: 'leaf' };
export type NavLinkBranch = { name: string; children: NavLinkLeaf[]; type: 'branch' };
export type NavLink = NavLinkLeaf | NavLinkBranch;
