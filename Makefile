# Build the project, opening it in the browser in development mode (with hot reload).
.PHONY: run
run: node_modules
	pnpm run dev

# Builds all code as a static site into build/.
.PHONY: build
build: node_modules
	pnpm run build

# Installs dependencies from the package.json.
node_modules: 
	pnpm install

# Remove all files that aren't committed to the git repository.
.PHONY: clean
clean:
	rm -rf node_modules
	rm -rf .svelte-kit
	rm -rf build
