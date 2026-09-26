import type { NavLink } from '../components/navigation/types';

export const links: NavLink[] = [
	{ name: 'Home', href: '/', type: 'leaf' },
	{
		name: 'Contact',
		type: 'branch',
		children: [
			{ name: 'Get In Touch', href: '/contact/get-in-touch', type: 'leaf' },
		]
	},
	{
		name: 'About',
		type: 'branch',
		children: [
			{ name: 'Publications', href: '/about/publications', type: 'leaf' },
			{ name: 'Our Group', href: '/about/our-group', type: 'leaf' }
		]
	}
];
