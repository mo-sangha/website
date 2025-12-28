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
			{ name: 'Lama Dawai Gocha', href: '/about/lama-dawai-gocha', type: 'leaf' },
			{ name: 'Publications', href: '/about/publications', type: 'leaf' },
			{ name: 'Curriculum', href: '/about/curriculum', type: 'leaf' },
			{ name: 'Our Lineage', href: '/about/our-lineage', type: 'leaf' },
			{ name: 'Our Group', href: '/about/our-group', type: 'leaf' }
		]
	}
];
