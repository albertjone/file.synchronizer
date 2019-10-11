#!/usr/bin/env python


def main():
    while 1:
        files = driver.get_all_files()
        db_files = db.get_all_files()
        need_updated, need_upload, need_deleted = process
