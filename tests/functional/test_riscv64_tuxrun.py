#!/usr/bin/env python3
#
# Functional test that boots known good tuxboot images the same way
# that tuxrun (www.tuxrun.org) does. This tool is used by things like
# the LKFT project to run regression tests on kernels.
#
# Copyright (c) 2023 Linaro Ltd.
#
# Author:
#  Alex Bennée <alex.bennee@linaro.org>
#
# SPDX-License-Identifier: GPL-2.0-or-later

from qemu_test import Asset
from qemu_test.tuxruntest import TuxRunBaselineTest

class TuxRunRiscV64Test(TuxRunBaselineTest):

    ASSET_RISCV64_KERNEL = Asset(
        'https://storage.tuxboot.com/20230331/riscv64/Image',
        'cd634badc65e52fb63465ec99e309c0de0369f0841b7d9486f9729e119bac25e')
    ASSET_RISCV64_ROOTFS = Asset(
        'https://storage.tuxboot.com/20230331/riscv64/rootfs.ext4.zst',
        'b18e3a3bdf27be03da0b285e84cb71bf09eca071c3a087b42884b6982ed679eb')

    ASSET_RISCV32_KERNEL = Asset(
        'https://storage.tuxboot.com/20230331/riscv32/Image',
        '89599407d7334de629a40e7ad6503c73670359eb5f5ae9d686353a3d6deccbd5')
    ASSET_RISCV32_ROOTFS = Asset(
        'https://storage.tuxboot.com/20230331/riscv32/rootfs.ext4.zst',
        '7168d296d0283238ea73cd5a775b3dd608e55e04c7b92b76ecce31bb13108cba')

    def test_riscv64(self):
        self.set_machine('virt')
        self.common_tuxrun(kernel_asset=self.ASSET_RISCV64_KERNEL,
                           rootfs_asset=self.ASSET_RISCV64_ROOTFS)

    def test_riscv64_maxcpu(self):
        self.set_machine('virt')
        self.cpu='max'
        self.common_tuxrun(kernel_asset=self.ASSET_RISCV64_KERNEL,
                           rootfs_asset=self.ASSET_RISCV64_ROOTFS)

    def test_riscv64_rv32(self):
        self.set_machine('virt')
        self.cpu='rv32'
        self.common_tuxrun(kernel_asset=self.ASSET_RISCV32_KERNEL,
                           rootfs_asset=self.ASSET_RISCV32_ROOTFS)

if __name__ == '__main__':
    TuxRunBaselineTest.main()
