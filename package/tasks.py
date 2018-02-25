#!/usr/bin/env python
# -*- coding: utf-8 -*-

import luigi


class ExtratZipfile(luigi.Task):
    path = luigi.IntParameter(default=1)

    def output(self):
        return luigi.LocalTarget("data/{}.tsv".format(self.path))

    def complete(self):
        pass

    def run(self):

        pass


class PreProcess(luigi.WrapperTask):
    def requires(self):
        yield ExtratZipfile()
