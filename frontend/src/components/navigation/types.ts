type NavLinkLeaf = { name: string; href: string };
type NavLinkBranch = { name: string; children: NavLinkLeaf[] };
export type NavLink = NavLinkLeaf | NavLinkBranch;