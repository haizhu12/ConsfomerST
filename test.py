import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util.visualizer import save_images
from util import html
import util.util as util
import time
import os

if __name__ == '__main__':
    opt = TestOptions().parse()  # get test options
    # hard-code some parameters for test
    opt.num_threads = 0   # test code only supports num_threads = 1
    opt.batch_size = 1    # test code only supports batch_size = 1
    opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
    opt.no_flip = True    # no flip; comment this line if results on flipped images are needed.
    opt.display_id = -1   # no visdom display; the test code saves the results to a HTML file.
    dataset = create_dataset(opt)  # create a dataset given opt.dataset_mode and other options
    # train_dataset = create_dataset(util.copyconf(opt, phase="train"))
    model = create_model(opt)      # create a model given opt.model and other options
    # create a webpage for viewing the results
    web_dir = os.path.join(opt.results_dir, opt.name, '{}_{}'.format(opt.phase, opt.epoch))  # define the website directory
    print('creating web directory', web_dir)
    webpage = html.HTML(web_dir, 'Experiment = %s, Phase = %s, Epoch = %s' % (opt.name, opt.phase, opt.epoch))

    filePath = 'datasets/dataset_A/testB'
    list_file_name = os.listdir(filePath)
    path_image = './datasets/dataset_A/testB/'

    for i, data in enumerate(dataset):
        #print(data['A_paths'])
        if i == 0:
            model.setup(opt)  # regular setup: load and print networks; create schedulers
            model.parallelize()
            if opt.eval:
                model.eval()
        if i >= opt.num_test:  # only apply our model to opt.num_test images.
            break
        for number in range(len(list_file_name)):
            data['B_paths'].pop()
            data['B_paths'].append(path_image+list_file_name[number])
            #file_full_path=path_image+list_file_name[number]



            model.set_input(data)  # unpack data from data loader
            time_x = 0
            start = time.time()
            model.test()           # run inference
            end = time.time()
            time_x = time_x + end - start
            print(end - start)
            visuals = model.get_current_visuals()  # get image results
            img_path = model.get_image_paths()     # get image paths
            if i % 1 == 0:  # save images to an HTML file
                print('processing (%04d)-th image... %s' % (i, img_path))

            save_images(webpage, visuals, img_path, width=opt.display_winsize)
    webpage.save()  # save the HTML


