import type { NavLink } from '../components/navigation/types';

export const links: NavLink[] = [
	{ name: 'Home', href: '/', type: 'leaf' },
	{
		name: 'Contact',
		type: 'branch',
		children: [
			{ name: 'Get In Touch', href: '/contact/get-in-touch', type: 'leaf' },
			{ name: 'Giving (Dana)', href: '/contact/giving', type: 'leaf' }
		]
	},
	{
		name: 'About',
		type: 'branch',
		children: [
			{ name: 'Dawai Gocha', href: '/about/dawai-gocha', type: 'leaf' },
			{ name: 'Our Lineage', href: '/about/our-lineage', type: 'leaf' },
			{ name: 'Our Group', href: '/about/our-group', type: 'leaf' }
		]
	}
];
