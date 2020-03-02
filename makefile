run: main.py display.py draw.py matrix.py parser.py pic_writer.py
	python pic_writer.py
	python main.py
	convert -delay 5 *.png thing.gif

clean:
	rm *.pyc
	rm *~
