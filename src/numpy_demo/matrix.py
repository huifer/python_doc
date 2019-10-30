#! /usr/bin/env python
# -*- coding: utf-8 -*-
# describe : 矩阵运算

import numpy as np


def plus(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """ 矩阵相加"""
    if x.shape == y.shape:
        return x + y


def multiply_matrix(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """矩阵×矩阵"""
    return x * y


def multiply_numb(x: np.ndarray, y: float) -> np.ndarray:
    """矩阵×数字"""
    return x * y


def multiply(x: np.ndarray, y) -> np.ndarray:
    """矩阵乘法"""
    return x.dot(y)


def transpose(x: np.ndarray) -> np.ndarray:
    """矩阵转置"""
    return x.T


def transpose2(x: np.ndarray) -> np.ndarray:
    """矩阵转置"""
    return x.transpose()


def det(x: np.ndarray) -> np.ndarray:
    """行列式"""
    return np.linalg.det(x)


def inv(x: np.ndarray) -> np.ndarray:
    """矩阵求逆"""
    return np.linalg.inv(x)


def inv2(x: np.ndarray) -> np.ndarray:
    """矩阵求逆"""
    # np.matrix()废弃
    return np.matrix(x).I


def rank(x: np.ndarray) :
    """矩阵rank"""
    return np.linalg.matrix_rank(x)


def trace(x: np.ndarray):
    """矩阵trace"""
    return np.trace(x)


