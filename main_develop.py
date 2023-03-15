'''
show video and Oscilloscope
'''
from Config import analysis_config_oscilloscope, config
from MP4_Tools import *
from multiprocessing import Process, Queue
from Oscilloscope_player import OscilloscopeLoader
import cv2
from mark_label import Marker
from multiprocessing import Process, Queue


def send_mese(q: Queue, message):
    q.put(str(message))


def main(config):
    start_frame = config['Start']
    show_oscilloscope_secen_time = config['Oscilloscope']['show_oscilloscope_secen_time']
    video_path = config['Video']['path']
    oscilloscope_data_list = analysis_config_oscilloscope(config)
    time_secs, time_nans, time_floats = get_video_time_(video_path)

    oscilloscopeLoader = OscilloscopeLoader(oscilloscope_data_list, show_oscilloscope_secen_time)
    SaveJsonPath = config['SaveJsonPath']
    q = Queue()

    maker = Marker(video_path, SaveJsonPath, q)
    cap = cv2.VideoCapture(video_path)
    Run = True
    index = 0
    while index < len(time_floats):
        time_frame = time_floats[index]

        if start_frame != None:
            while int(time_frame) < start_frame:
                index += 1
                time_frame = time_floats[index]
                print(int(time_frame), start_frame, index)
            cap.set(cv2.CAP_PROP_POS_FRAMES, index)
            start_frame = None
        if Run:
            statu, frame = cap.read()
            index += 1
        else:

            if key == 81 or key == 97:
                q.put(str(time_frame))

                index -= 5
                cap.set(cv2.CAP_PROP_POS_FRAMES, index)
                _, _ = cap.read()
                statu, frame = cap.read()
                oscilloscopeLoader.make_oscilloscope(time_frame)
                cv2.imshow('frame', frame)
            if key == 83 or key == 100:
                q.put(str(time_frame))

                index += 5
                oscilloscopeLoader.make_oscilloscope(time_frame)
                cap.set(cv2.CAP_PROP_POS_FRAMES, index)
                _, _ = cap.read()
                statu, frame = cap.read()
                cv2.imshow('frame', frame)
        if index % 5 == 0:
            oscilloscopeLoader.make_oscilloscope(time_frame)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if key == 32:
            q.put(str(time_frame))
            Run = bool(1 - Run)
    maker.kill()


if __name__ == '__main__':
    main(config)
