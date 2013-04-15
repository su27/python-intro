slides_python:
	@python template/make_slides.py < template/index.tmpl > pages/index.html
	@python template/make_clean_md.py < src/python-intro-remark.md > README.md
