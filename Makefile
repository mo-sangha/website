# Build the project, opening it in the browser in development mode (with hot reload).
.PHONY: run
run: node_modules
	npm run dev -- --open

# Builds all code as a static site into build/.
.PHONY: build
build: node_modules
	npm run build

# Installs dependencies from the package.json.
node_modules: 
	npm install

# Remove all files that aren't committed to the git repository.
.PHONY: clean
clean:
	rm -rf node_modules
	rm -rf .svelte-kit
	rm -rf build
