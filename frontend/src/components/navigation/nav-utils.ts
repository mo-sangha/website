import type { NavLink } from './types';
import type { Page } from '@sveltejs/kit';

export const isActive = (link: NavLink, page: Page): boolean => {
	if ('children' in link) {
		return link.children.some((link) => isActive(link, page));
	}

	return link.href === page.url.pathname;
};
