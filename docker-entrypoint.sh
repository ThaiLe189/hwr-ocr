echo 'MAKE FOLDERS'
INPUT=./input
if [ -d "$INPUT" ]; then
    echo "$INPUT exists."
else
    mkdir -p $INPUT 
fi
LOG=./log
if [ -d "$LOG" ]; then
    echo "$LOG exists."
else
    mkdir -p $LOG 
fi
OUTPUT=./output
if [ -d "$OUTPUT" ]; then
    echo "$OUTPUT exists."
else
    mkdir -p $OUTPUT 
fi
echo 'RUN SERVER'
#gunicorn --chdir app app:app -w 2 --threads 2 -b 0.0.0.0:5000
python app.py
streamlit run FE.py --server.port=8501 --server.address=0.0.0.0