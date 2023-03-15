import os
import pandas as pd

config = {
    'Start': None,
    'Video': {
        'path': r'C:\Users\NailinLiao\Desktop\G3\rec_0330008_default_2023-02-07-18_57_09_0_1.avi',
    },  # rec_0330008_2023-02-07-18_57_03
    'Oscilloscope':
        {
            'Radar_path': r'C:\Users\NailinLiao\Desktop\G3\can_output',
            'show_oscilloscope_secen_time': 10,
            'select': {
                'ADCU3A_St7': [
                    # 'ADCU3A_FCWAEBWarnLvl',
                    # 'ADCU3A_FCWWrkSt',
                    # 'ADCU3A_AEBTrgType', #有问题 'No Trigger' 'No Trigger' 'No Trigger' 'No Trigger' 'No Trigger'
                    'ADCU3A_AEBTypeTar',
                    'ADCU3A_AEBRelDst',
                    # 'ADCU3A_AEBRelSpd',
                    # 'ADCU3A_AEBTTC'
                ],
                # 'ADCU3B_LgtdCtrl': [
                #     'ADCU3BA_LgtdCtrl_CRC'
                # ],
                # 'ADCU3A_Test': [
                #     # 'ADCU3A_FCWInhibitNum',
                #     # 'ADCU3A_FCWMode',
                #     # 'ADCU3A_FCW1Dist',
                #     # 'ADCU3A_FCW2Dist',
                #     # 'ADCU3A_FCW3Dist',
                #     # 'ADCU3A_FCWAvoidAcc',
                #     # 'ADCU3A_AEBInhibitNum',
                #     # 'ADCU3A_AEBMode',
                #     'ADCU3A_AEBDist',
                #     # 'ADCU3A_FCWCIP',
                #     # 'ADCU3A_FCWTargetID',
                #     # 'ADCU3A_FCWRelDisX',
                #     # 'ADCU3A_FCWRelSpdX',
                #     # 'ADCU3A_FCWOffset',
                #     # 'ADCU3A_FCWRelDisY',
                #     # 'ADCU3A_FCWRelSpdY',
                #     # 'ADCU3A_AEBCIP',
                #     # 'ADCU3A_AEBTargetID',
                #     # 'ADCU3A_AEBRelDisX',
                #     # 'ADCU3A_AEBRelSpdX',
                #     # 'ADCU3A_AEBOffset',
                #     # 'ADCU3A_AEBRelDisY',
                #     'ADCU3A_AEBRelSpdY',
                # ],
                # HZ：1，30，60,140

                # 'ADCU3A_XBR': [
                #     'ExtAcclCmd'
                # ]
            }
        },
    'SaveJsonPath': './json_label',
    'label_list': [' '],
}

json_struct = {
    'video_name': None,
    'label': [
        # ['cut_int', 12345, 12345],
        # ['cut_int', 12345, 12345],
        # ['cut_int', 12345, 12345],
    ],
    'Modification_time': None,
}


def analysis_config_oscilloscope(config):
    '''
    解析配置文件中要求展示的波形数据
    '''
    Radar_path = config['Oscilloscope']['Radar_path']
    oscilloscope = config['Oscilloscope']['select']

    oscilloscope_data_list = []
    csv_file_list = os.listdir(Radar_path)
    # vidie_file_name = str(os.path.split(config['Video']['path'])[-1]).split('.')[0]
    start_frame_time = '-'.join(str(os.path.split(config['Video']['path'])[-1]).split('_')[4:-2])
    for key in oscilloscope:
        for csv_file in csv_file_list:
            if key in csv_file and start_frame_time in csv_file:
            # if key in csv_file:
                csv_path = os.path.join(Radar_path, csv_file)
                DataFrame = pd.read_csv(csv_path)
                property_list = oscilloscope[key]
                for property in property_list:
                    oscilloscope_data_list.append([property, DataFrame])
    return oscilloscope_data_list
