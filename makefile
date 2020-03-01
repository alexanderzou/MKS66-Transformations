run: main.py display.py draw.py matrix.py parser.py
	python pic_writer.py
	python main.py

clean:
	rm *.pyc
	rm *~
