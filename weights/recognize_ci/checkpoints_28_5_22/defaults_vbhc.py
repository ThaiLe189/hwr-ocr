"""
Default parameters
"""


class Config:

    GPU_ID = -1
    VISUALIZE = False

    # I/O
    NEW_DATASET_PATH = 'dataset.tfrecords'
    DATA_PATH = 'data.tfrecords'
    MODEL_DIR = 'checkpoints'
    LOG_PATH = 'attentionocr.log'
    OUTPUT_DIR = 'results'
   
    EXPORT_FORMAT = 'savedmodel'
    EXPORT_PATH = 'exported'
    FORCE_UPPERCASE = True
    SAVE_FILENAME = False
    FULL_ASCII = False

    # Optimization
    if 1<0: #bao giờ ok thì thay lại thành if 1>0:
    # if 1>0:
        NUM_EPOCH =20 #5000 
        STEPS_PER_CHECKPOINT =10  #100
        # Dataset generation
        LOG_STEP = 500 #500
    else:
        NUM_EPOCH = 10000
        STEPS_PER_CHECKPOINT = 100
        LOG_STEP=1000
    #lần đầu chạy thì ko nên đặt quá lớn, và ko nên để 5000, mà phải đê nhỏ thôi, 100? và xem model ghi ? rồi load lại ?

    BATCH_SIZE = 16#65#số này rất quan trọng
    INITIAL_LEARNING_RATE = 1.0

    # Network parameters
    CLIP_GRADIENTS = True  # whether to perform gradient clipping
    MAX_GRADIENT_NORM = 5.0  # Clip gradients to this norm
    TARGET_EMBEDDING_SIZE = 10  # embedding dimension for each target
    ATTN_USE_LSTM = True  # whether or not use LSTM attention decoder cell
    ATTN_NUM_HIDDEN = 128  # number of hidden units in attention decoder cell
    ATTN_NUM_LAYERS = 2  # number of layers in attention decoder cell
    # (Encoder number of hidden units will be ATTN_NUM_HIDDEN*ATTN_NUM_LAYERS)
    LOAD_MODEL = True
    OLD_MODEL_VERSION = False
    #TARGET_VOCAB_SIZE = 26+10+3  # 0: PADDING, 1: GO, 2: EOS, >2: 0-9, a-z#cái này cho tiếng Anh, sửa phải để ý
    #thơm
    if 1<0: #digit
        TARGET_VOCAB_SIZE = 3+10# CHARMAP = ['', '', ''] + list('012345678')
    else:
        #TARGET_VOCAB_SIZE = 3+5+186# CHARMAP = ['', '', ''] + list(' -,:()/')+list('0123456789ABCDEFGHIKLMNOPQRSTUVXYabcdeghijklmnopqrstuvxyÀÁÂÃÊÌÍÒÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẬậẮắẰằẵẶặẻẾếỀềỂểỄễỆệỈỉỊịỌọỏỐốỒồổỖỗỘộỚớỜờỞởỢợỤụỦủỨứỪừỬửỮữỰựỲỳỸỹ')        
        #CHARMAP = ['', '', ''] + list(" '-.:ABCDEGHIJKLMNOPQRSTUVXYhinotÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝêĂĐĨŨƠƯẠẢẤẦẨẪẬẮẰẶẸẾỀỂỄỆỈỊỌọỎỐỒỔỖỘỚỜỞỢỤỦỨỪỬỮỰỲỶỸ")        
        # TARGET_VOCAB_SIZE=3+10+247 #goc
        TARGET_VOCAB_SIZE=3+10+247
        #h_log(TARGET_VOCAB_SIZE)


    CHANNELS = 3# number of color channels from source image (1 = grayscale, 3 = rgb)
    #thơm
    # CHANNELS = 3 #ảnh đầu vào hiện đang là ảnh mầu
    #MAX_WIDTH = 160
    #thơm
    MAX_WIDTH = 2200#ài   25.03.2020  ok
    # MAX_WIDTH = 1300
    # MAX_HEIGHT = 120
    #MAX_HEIGHT = 60
    #thơm
    MAX_HEIGHT =200# thể nhận 2 dòng 25.03.2020 ok
    #MAX_PREDICTION = 20
    #thơm
    MAX_PREDICTION = 197
    # MAX_PREDICTION = 160
    USE_DISTANCE = True

    