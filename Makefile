slides_python:
	@python template/make_slides.py < template/index.tmpl > index.html
	@python template/make_clean_md.py < src/python-intro-remark.md > python-intro.md
