#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys

import numpy as np
import tensorflow as tf

from PIL import Image
from six import BytesIO as IO

from .bucketdata import BucketData

try:
    TFRecordDataset = tf.data.TFRecordDataset  # pylint: disable=invalid-name
except AttributeError:
    TFRecordDataset = tf.contrib.data.TFRecordDataset  # pylint: disable=invalid-name
class DataGen(object):
    GO_ID = 1
    EOS_ID = 2
    IMAGE_HEIGHT = 32
    if 1<0: #digit 
        CHARMAP = ['', '', ''] + list('0123456789')
    else:
        #Số CMND_ Mới
        # CHARMAP = ['', '', ''] + list(" !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~«®°²µÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỵỶỷỸỹ—‘“”…›≤")
        # Địa chỉ CMND cũ

        # CHARMAP = ['', '', ''] + list(' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỵỶỷỸỹ—“”…›≤')


        # CHARMAP = ['', '', ''] + list(' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ—“”…›≤')+ list("'")+list("'")# đang huấn luyện
        #vbhc_6_10
        # CHARMAP = ['', '', ''] + list(' !"#$%&')+  list("'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ—“”…›≤")
        # CHARMAP = ['', '', ''] + list(' !"#$%&')+  list("'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯự̀́ΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ–—“”†…›≤")
        # CHARMAP = ['', '', ''] + list(' !"#$%&')+  list("'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯự̀́ΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ–—‘“”†…›≤")
        # CHARMAP = ['', '', ''] + list(' !"#$%&')+  list("'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕ×ÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯự̀́̃̉ΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ–—‘“”†…›→−□")
        # CHARMAP = ['', '', ''] + list(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~«®°±²³µ»¼ÀÁÂÃÈÉÊÌÍÐÒÓÔÕ×ØÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯư˜̣̀́̃̉ΓΦαδλπτφϵᵒᵩẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ–—―‘’“”„†•…›⁰℃↑→↓↘∑−∙√≠≤≥□△')
        CHARMAP = ['', '', ''] + list(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~«®°²µ·»ÀÁÂÃÈÉÊÌÍÒÓÔÕ×ÙÚÝßàáâãèéêìíòóôõöùúýĂăĐđĨĩŨũƠơƯự̀́̃̉ΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ–—‘“”†…›→−□')
        # CHARMAP = ['', '', ''] + list(' !"#$%&')+  list("'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯự̀́ΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ–—‘“”†…›")
        ## CHARMAP = ['', '', ''] + list(' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ—“”…›≤')+ list("'")+list("'")# đang huấn luyện
        # CHARMAP = ['', '', ''] + list(' !"#$%&')+  list("'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~«®°²µ»ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝßàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯự̀́ΓαπτẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ–—“”…›≤")
        # CHARMAP=['', '', '']+ list(" !#%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]_abcdefghijklmnopqrstuvwxyz{}~®°²ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỵỶỷỸỹ—”…")
        #bctc
        # CHARMAP=['', '', '']+ list(" !#%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]abcdefghijklmnopqrstuvwxyz{}°²ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẳẴẵẶặẸẹẺẻẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỵỶỷỸỹ—†…›")
    @staticmethod
    def set_full_ascii_charmap():
        DataGen.CHARMAP =CHARMAP

    def __init__(self,
                 annotation_fn,
                 buckets,
                 epochs=1000,
                 max_width=None):
        """
        :param annotation_fn:
        :param lexicon_fn:
        :param valid_target_len:
        :param img_width_range: only needed for training set
        :param word_len:
        :param epochs:
        :return:
        """
        self.epochs = epochs
        self.max_width = max_width

        self.bucket_specs = buckets
        self.bucket_data = BucketData()

        dataset = TFRecordDataset([annotation_fn])
        dataset = dataset.map(self._parse_record)
        dataset = dataset.shuffle(buffer_size=1000)
        self.dataset = dataset.repeat(self.epochs)

    def clear(self):
        self.bucket_data = BucketData()

    def gen(self, batch_size):

        dataset = self.dataset.batch(batch_size)
        iterator = dataset.make_one_shot_iterator()

        images, labels, comments = iterator.get_next()
        with tf.Session(config=tf.ConfigProto(allow_soft_placement=True)) as sess:

            while True:
                try:
                    raw_images, raw_labels, raw_comments = sess.run([images, labels, comments])
                    for img, lex, comment in zip(raw_images, raw_labels, raw_comments):

                        if self.max_width and (Image.open(IO(img)).size[0] <= self.max_width):
                            word = self.convert_lex(lex)

                            bucket_size = self.bucket_data.append(img, word, lex, comment)
                            if bucket_size >= batch_size:
                                bucket = self.bucket_data.flush_out(
                                    self.bucket_specs,
                                    go_shift=1)
                                yield bucket

                except tf.errors.OutOfRangeError:
                    break

        self.clear()

    def convert_lex(self,lex):
        if sys.version_info >= (3,):
            lex = lex.decode('utf-8')
        assert len(lex) < self.bucket_specs[-1][1]
        return np.array(
            [self.GO_ID] + [self.CHARMAP.index(char) for char in lex] + [self.EOS_ID],
            dtype=np.int32)
        # # return 
    @staticmethod
    def _parse_record(example_proto):
        features = tf.parse_single_example(
            example_proto,
            features={
                'image': tf.FixedLenFeature([], tf.string),
                'label': tf.FixedLenFeature([], tf.string),
                'comment': tf.FixedLenFeature([], tf.string, default_value=''),
            })
        return features['image'], features['label'], features['comment']