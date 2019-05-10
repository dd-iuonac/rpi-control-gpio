if __name__ == '__main__':
    import sys
    from package.app import Application

    application = Application(sys.argv)
    sys.exit(application.exec_())


