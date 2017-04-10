import argparse
from bruker2nifti.study_converter import convert_a_study


def main():
    """
    Parser from terminal with

    $ python2 bruker2nifti_study -i input_file_path -o output_file_path
    """

    parser = argparse.ArgumentParser(version=0.0)

    # pfo_study_bruker_input
    parser.add_argument('-i', '--input_study_folder',
                        dest='pfo_input',
                        type=str,
                        required=True,
                        help='Bruker study folder.')

    # pfo_study_nifti_output
    parser.add_argument('-o', '--output_study_folder',
                        dest='pfo_output',
                        type=str,
                        required=True,
                        help='Output folder where the study will be saved.')

    # study_name = None,
    parser.add_argument('-study_name',
                        dest='study_name',
                        type=str,
                        default=None)

    # scans_list = None
    parser.add_argument('-scans_list',
                        dest='scans_list',
                        type=list,
                        default=None)

    # list_new_name_each_scan = None,
    parser.add_argument('-list_new_name_each_scan',
                        dest='list_new_name_each_scan',
                        type=list,
                        default=None)

    # nifti_version = 1,
    parser.add_argument('-nifti_version',
                        dest='nifti_version',
                        type=int,
                        default=1)

    # qform = 2,
    parser.add_argument('-qform',
                        dest='qform',
                        type=int,
                        default=2)

    # sform= 1,
    parser.add_argument('-sform',
                        dest='sform',
                        type=int,
                        default=1)

    # axis_direction = (-1, -1, 1),
    parser.add_argument('-axis_direction',
                        dest='axis_direction',
                        type=tuple,
                        default=(-1, -1, 1))

    # save_human_readable = True,
    parser.add_argument('-save_human_readable',
                        dest='save_human_readable',
                        action='store_true')

    # normalise_b_vectors_if_dwi = True,
    parser.add_argument('-normalise_b_vectors_if_dwi',
                        dest='normalise_b_vectors_if_dwi',
                        action='store_true')

    # correct_slope = False,
    parser.add_argument('-correct_slope',
                        dest='correct_slope',
                        action='store_false')
    # verbose = 1
    parser.add_argument('-scans_list',
                        dest='scans_list',
                        action='store_true')

    # Parse the input arguments
    args = parser.parse_args()

    # Apply to the study:
    convert_a_study(args.pfo_input,
                    args.pfo_output,
                    study_name=args.study_name,
                    scans_list=args.scans_list,
                    list_new_name_each_scan=args.list_new_name_each_scan,
                    nifti_version=args.nifti_version,
                    qform=args.qform,
                    sform=args.sform,
                    axis_direction=args.axis_direction,
                    save_human_readable=args.save_human_readable,
                    normalise_b_vectors_if_dwi=args.normalise_b_vectors_if_dwi,
                    correct_slope=args.correct_slope,
                    verbose=args.verbose
                    )

if __name__ == "__main__":
    main()