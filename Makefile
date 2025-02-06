build:
	mkdir -p themes
	python3 src/build.py

package: build
	vsce package

publish: package
	vsce publish

clean:
	rm -f *.vsix themes/*.json
	rm -rf src/__pycache__

.PHONY: build package publish clean
