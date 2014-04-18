#!/usr/bin/env python

import argparse
import numpy as np
import scipy as sp
import scipy.stats as stat
import matplotlib.pyplot as pl


def parse_script_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s',
                        action='store',
                        type=int,
                        dest='dataset_size',
                        default=1000,
                        help='Size of simulated dataset')
    parser.add_argument('--min_x',
                        action='store',
                        type=float,
                        dest='min_x',
                        default=-100,
                        help='Minimal value of independent variable')
    parser.add_argument('--max_x',
                        action='store',
                        type=float,
                        dest='max_x',
                        default=100,
                        help='Maximal value of independent variable')
    parser.add_argument('-a',
                        action='store',
                        type=float,
                        dest='alpha',
                        default=4.5,
                        help='Alpha value for dataset. y = ax + b')
    parser.add_argument('-b',
                        action='store',
                        type=float,
                        dest='beta',
                        default=-2.8,
                        help='Beta value for dataset. y = ax + b')
    parser.add_argument('--sigma',
                        action='store',
                        type=float,
                        dest='sigma',
                        default=80,
                        help='Sigma value for noise')
    parser.add_argument('-mu',
                        action='store',
                        type=float,
                        dest='mu',
                        default=0,
                        help='Mean value for noise')
    return parser


def generate_linear_dataset_with_deviations(size, min_x, max_x,  alpha, beta, sigma, mu):
    x = (max_x - min_x) * np.random.random_sample((size)) + min_x
    y = alpha * x + beta
    deviation = sigma*sp.randn(size) + mu
    return x, y, y + deviation


def save_data(x, y, y_dev, learn_set_size, x_prefix="x", y_prefix="y", y_dev_prefix="ydev"):
    for data, data_prefix in (x, x_prefix), (y, y_prefix), (y_dev, y_dev_prefix):
        with open("%s_learn.t" % data_prefix, "wb") as fd:
            np.savetxt(fd, data[:learn_set_size])
        with open("%s_test.t" % data_prefix, "wb") as fd:
            np.savetxt(fd, data[:learn_set_size])


def construct_linear_regression(x_learn, y_dev_learn, x_test, y_dev_test):

    regression = sp.polyfit(x_learn, y_dev_learn, 1)

    y_exp_learn = sp.polyval(regression, x_learn)
    y_exp_test = sp.polyval(regression, x_test)

    print("For train dataset:\n\ty = a*x + b\n\ta = %f\n\tb = %f" % (regression[0], regression[1]))

    mse_learn = np.sqrt(np.mean((y_exp_learn - y_dev_learn) ** 2))
    mse_test = np.sqrt(np.mean((y_exp_test - y_dev_test) ** 2))
    mse_total = np.sqrt((((mse_learn**2) * learn_set_size)
                         + ((mse_test**2) * (dataset_size - learn_set_size)))
                        / dataset_size)
    print("Train MSE = %f\nTest MSE = %f\nTotal MSE = %f" % (mse_learn, mse_test,mse_total ))
    return regression, mse_learn, mse_test, mse_total, y_exp_learn, y_exp_test


def draw_plots(x_learn, y_dev_learn, y_exp_learn, x_test, y_dev_test, y_exp_test, x, y):
    learn_plot, = pl.plot(x_learn, y_dev_learn, 'b.')
    test_plot, = pl.plot(x_test, y_dev_test, 'g.')
    theoretical_line_plot, = pl.plot(x, y, 'r-')
    empirical_line_plot, = pl.plot(x, np.hstack((y_exp_learn,y_exp_test)), 'c-')
    pl.xlabel('X')
    pl.ylabel('Y')
    pl.legend([learn_plot, test_plot, theoretical_line_plot, empirical_line_plot],
              ["train data", "test data", "theoretical regression", "empirical regression"], loc="upper left")
    pl.savefig('regression.png', format='png')


def draw_deviations(x, y_dev, y_emp, error):
    y_subtract = np.abs(y_dev - y_emp)
    in_interval = []
    out_of_interval = []
    for i in range(0, len(y_subtract)):
        if y_subtract[i] < error:
            in_interval.append([x[i], y_dev[i]])
        else:
            out_of_interval.append([x[i], y_dev[i]])
    in_interval = np.array(in_interval)
    out_of_interval = np.array(out_of_interval)

    in_interval_plot, = pl.plot(in_interval[:, 0], in_interval[:, 1], 'b.')
    out_of_interval_plot, = pl.plot(out_of_interval[:, 0], out_of_interval[:, 1], 'g.')
    regeression_line_plot, = pl.plot(x, y_emp, 'r-')
    pl.xlabel('X')
    pl.ylabel('Y')
    pl.legend([in_interval_plot, out_of_interval_plot, regeression_line_plot],
              ["points within MSE", "point out of MSE", "regresion"], loc="upper left")
    pl.savefig('interval.png', format='png')


if __name__ == "__main__":
    parser = parse_script_arg()
    arguments = parser.parse_args()

    dataset_size = arguments.dataset_size
    min_x = arguments.min_x
    max_x = arguments.max_x
    alpha = arguments.alpha
    beta = arguments.beta
    sigma = arguments.sigma
    mu = arguments.mu
    learn_set_size = int(dataset_size/2)
    sig_level = 0.05

    parameters_string = "dataset_size\t%i\nmin_x\t%f\nmax_x\t%f\nalpha\t%f\nbeta\t%f\nlearn_set_size\t%i\n" %\
                        (dataset_size, min_x, max_x, alpha, beta, learn_set_size)
    parameters_string += "noise_mu\t%f\nnoise_sigma\t%f\n" % (mu, sigma)
    with open("parameters.t", "w") as fd:
        fd.write(parameters_string)
    print("\nInput parameters:\n%s" % parameters_string)

    print("\nGenerating dataset...")
    x, y, y_dev = generate_linear_dataset_with_deviations(dataset_size, min_x, max_x,  alpha, beta, sigma, mu)
    save_data(x, y, y_dev, learn_set_size)

    print("\nConstructing regression...")
    regression, mse_learn, mse_test, mse_total, \
                        y_exp_learn, y_exp_test = construct_linear_regression(x[:learn_set_size],
                                                                              y_dev[:learn_set_size],
                                                                              x[learn_set_size:],
                                                                              y_dev[learn_set_size:])

    print("Calculating coefficients for total dataset...")
    exp_alpha, exp_beta, r_value, p_value, std_err = stat.linregress(x, y_dev)
    t_student = r_value * np.sqrt(dataset_size-2) / (1 - r_value**2)
    print("For total dataset:\n\ty = a*x + b\n\ta = %f\n\tb = %f\n\tr = %f\n\tR2 = %f"
          % (exp_alpha, exp_beta, r_value, r_value**2))
    print("\tStudent's t = %f\n\tp-value = %f\n\tsig_level = %f" % (t_student, p_value, sig_level))

    draw_plots(x[:learn_set_size], y_dev[:learn_set_size], y_exp_learn,
               x[learn_set_size:], y_dev[learn_set_size:], y_exp_test,
               x, y)

    draw_deviations(x, y_dev,
                    np.hstack((y_exp_learn, y_exp_test)),
                    mse_total)