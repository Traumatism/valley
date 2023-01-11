SYS_syscall = 0
SYS_exit = 1
SYS_fork = 2
SYS_read = 3
SYS_write = 4
SYS_open = 5
SYS_close = 6
SYS_wait4 = 7
SYS_link = 9
SYS_unlink = 10
SYS_chdir = 12
SYS_fchdir = 13
SYS_mknod = 14
SYS_chmod = 15
SYS_chown = 16
SYS_getfsstat = 18
SYS_getpid = 20
SYS_setuid = 23
SYS_getuid = 24
SYS_geteuid = 25
SYS_ptrace = 26
SYS_recvmsg = 27
SYS_sendmsg = 28
SYS_recvfrom = 29
SYS_accept = 30
SYS_getpeername = 31
SYS_getsockname = 32
SYS_access = 33
SYS_chflags = 34
SYS_fchflags = 35
SYS_sync = 36
SYS_kill = 37
SYS_getppid = 39
SYS_dup = 41
SYS_pipe = 42
SYS_getegid = 43
SYS_sigaction = 46
SYS_getgid = 47
SYS_sigprocmask = 48
SYS_getlogin = 49
SYS_setlogin = 50
SYS_acct = 51
SYS_sigpending = 52
SYS_sigaltstack = 53
SYS_ioctl = 54
SYS_reboot = 55
SYS_revoke = 56
SYS_symlink = 57
SYS_readlink = 58
SYS_execve = 59
SYS_umask = 60
SYS_chroot = 61
SYS_msync = 65
SYS_vfork = 66
SYS_munmap = 73
SYS_mprotect = 74
SYS_madvise = 75
SYS_mincore = 78
SYS_getgroups = 79
SYS_setgroups = 80
SYS_getpgrp = 81
SYS_setpgid = 82
SYS_setitimer = 83
SYS_swapon = 85
SYS_getitimer = 86
SYS_getdtablesize = 89
SYS_dup2 = 90
SYS_fcntl = 92
SYS_select = 93
SYS_fsync = 95
SYS_setpriority = 96
SYS_socket = 97
SYS_connect = 98
SYS_getpriority = 100
SYS_bind = 104
SYS_setsockopt = 105
SYS_listen = 106
SYS_sigsuspend = 111
SYS_gettimeofday = 116
SYS_getrusage = 117
SYS_getsockopt = 118
SYS_readv = 120
SYS_writev = 121
SYS_settimeofday = 122
SYS_fchown = 123
SYS_fchmod = 124
SYS_setreuid = 126
SYS_setregid = 127
SYS_rename = 128
SYS_flock = 131
SYS_mkfifo = 132
SYS_sendto = 133
SYS_shutdown = 134
SYS_socketpair = 135
SYS_mkdir = 136
SYS_rmdir = 137
SYS_utimes = 138
SYS_futimes = 139
SYS_adjtime = 140
SYS_gethostuuid = 142
SYS_setsid = 147
SYS_getpgid = 151
SYS_setprivexec = 152
SYS_pread = 153
SYS_pwrite = 154
SYS_nfssvc = 155
SYS_statfs = 157
SYS_fstatfs = 158
SYS_unmount = 159
SYS_getfh = 161
SYS_quotactl = 165
SYS_mount = 167
SYS_csops = 169
SYS_csops_audittoken = 170
SYS_waitid = 173
SYS_kdebug_typefilter = 177
SYS_kdebug_trace_string = 178
SYS_kdebug_trace64 = 179
SYS_kdebug_trace = 180
SYS_setgid = 181
SYS_setegid = 182
SYS_seteuid = 183
SYS_sigreturn = 184
SYS_thread_selfcounts = 186
SYS_fdatasync = 187
SYS_stat = 188
SYS_fstat = 189
SYS_lstat = 190
SYS_pathconf = 191
SYS_fpathconf = 192
SYS_getrlimit = 194
SYS_setrlimit = 195
SYS_getdirentries = 196
SYS_mmap = 197
SYS_lseek = 199
SYS_truncate = 200
SYS_ftruncate = 201
SYS_sysctl = 202
SYS_mlock = 203
SYS_munlock = 204
SYS_undelete = 205
SYS_open_dprotected_np = 216
SYS_fsgetpath_ext = 217
SYS_openat_dprotected_np = 218
SYS_getattrlist = 220
SYS_setattrlist = 221
SYS_getdirentriesattr = 222
SYS_exchangedata = 223
SYS_searchfs = 225
SYS_delete = 226
SYS_copyfile = 227
SYS_fgetattrlist = 228
SYS_fsetattrlist = 229
SYS_poll = 230
SYS_getxattr = 234
SYS_fgetxattr = 235
SYS_setxattr = 236
SYS_fsetxattr = 237
SYS_removexattr = 238
SYS_fremovexattr = 239
SYS_listxattr = 240
SYS_flistxattr = 241
SYS_fsctl = 242
SYS_initgroups = 243
SYS_posix_spawn = 244
SYS_ffsctl = 245
SYS_fhopen = 248
SYS_minherit = 250
SYS_semsys = 251
SYS_msgsys = 252
SYS_shmsys = 253
SYS_semctl = 254
SYS_semget = 255
SYS_semop = 256
SYS_msgctl = 258
SYS_msgget = 259
SYS_msgsnd = 260
SYS_msgrcv = 261
SYS_shmat = 262
SYS_shmctl = 263
SYS_shmdt = 264
SYS_shmget = 265
SYS_shm_open = 266
SYS_shm_unlink = 267
SYS_sem_open = 268
SYS_sem_close = 269
SYS_sem_unlink = 270
SYS_sem_wait = 271
SYS_sem_trywait = 272
SYS_sem_post = 273
SYS_sysctlbyname = 274
SYS_open_extended = 277
SYS_umask_extended = 278
SYS_stat_extended = 279
SYS_lstat_extended = 280
SYS_fstat_extended = 281
SYS_chmod_extended = 282
SYS_fchmod_extended = 283
SYS_access_extended = 284
SYS_settid = 285
SYS_gettid = 286
SYS_setsgroups = 287
SYS_getsgroups = 288
SYS_setwgroups = 289
SYS_getwgroups = 290
SYS_mkfifo_extended = 291
SYS_mkdir_extended = 292
SYS_identitysvc = 293
SYS_shared_region_check_np = 294
SYS_vm_pressure_monitor = 296
SYS_psynch_rw_longrdlock = 297
SYS_psynch_rw_yieldwrlock = 298
SYS_psynch_rw_downgrade = 299
SYS_psynch_rw_upgrade = 300
SYS_psynch_mutexwait = 301
SYS_psynch_mutexdrop = 302
SYS_psynch_cvbroad = 303
SYS_psynch_cvsignal = 304
SYS_psynch_cvwait = 305
SYS_psynch_rw_rdlock = 306
SYS_psynch_rw_wrlock = 307
SYS_psynch_rw_unlock = 308
SYS_psynch_rw_unlock2 = 309
SYS_getsid = 310
SYS_settid_with_pid = 311
SYS_psynch_cvclrprepost = 312
SYS_aio_fsync = 313
SYS_aio_return = 314
SYS_aio_suspend = 315
SYS_aio_cancel = 316
SYS_aio_error = 317
SYS_aio_read = 318
SYS_aio_write = 319
SYS_lio_listio = 320
SYS_iopolicysys = 322
SYS_process_policy = 323
SYS_mlockall = 324
SYS_munlockall = 325
SYS_issetugid = 327
SYS___pthread_kill = 328
SYS___pthread_sigmask = 329
SYS___sigwait = 330
SYS___disable_threadsignal = 331
SYS___pthread_markcancel = 332
SYS___pthread_canceled = 333
SYS___semwait_signal = 334
SYS_proc_info = 336
SYS_sendfile = 337
SYS_stat64 = 338
SYS_fstat64 = 339
SYS_lstat64 = 340
SYS_stat64_extended = 341
SYS_lstat64_extended = 342
SYS_fstat64_extended = 343
SYS_getdirentries64 = 344
SYS_statfs64 = 345
SYS_fstatfs64 = 346
SYS_getfsstat64 = 347
SYS___pthread_chdir = 348
SYS___pthread_fchdir = 349
SYS_audit = 350
SYS_auditon = 351
SYS_getauid = 353
SYS_setauid = 354
SYS_getaudit_addr = 357
SYS_setaudit_addr = 358
SYS_auditctl = 359
SYS_bsdthread_create = 360
SYS_bsdthread_terminate = 361
SYS_kqueue = 362
SYS_kevent = 363
SYS_lchown = 364
SYS_bsdthread_register = 366
SYS_workq_open = 367
SYS_workq_kernreturn = 368
SYS_kevent64 = 369
SYS_thread_selfid = 372
SYS_ledger = 373
SYS_kevent_qos = 374
SYS_kevent_id = 375
SYS___mac_execve = 380
SYS___mac_syscall = 381
SYS___mac_get_file = 382
SYS___mac_set_file = 383
SYS___mac_get_link = 384
SYS___mac_set_link = 385
SYS___mac_get_proc = 386
SYS___mac_set_proc = 387
SYS___mac_get_fd = 388
SYS___mac_set_fd = 389
SYS___mac_get_pid = 390
SYS_pselect = 394
SYS_pselect_nocancel = 395
SYS_read_nocancel = 396
SYS_write_nocancel = 397
SYS_open_nocancel = 398
SYS_close_nocancel = 399
SYS_wait4_nocancel = 400
SYS_recvmsg_nocancel = 401
SYS_sendmsg_nocancel = 402
SYS_recvfrom_nocancel = 403
SYS_accept_nocancel = 404
SYS_msync_nocancel = 405
SYS_fcntl_nocancel = 406
SYS_select_nocancel = 407
SYS_fsync_nocancel = 408
SYS_connect_nocancel = 409
SYS_sigsuspend_nocancel = 410
SYS_readv_nocancel = 411
SYS_writev_nocancel = 412
SYS_sendto_nocancel = 413
SYS_pread_nocancel = 414
SYS_pwrite_nocancel = 415
SYS_waitid_nocancel = 416
SYS_poll_nocancel = 417
SYS_msgsnd_nocancel = 418
SYS_msgrcv_nocancel = 419
SYS_sem_wait_nocancel = 420
SYS_aio_suspend_nocancel = 421
SYS___sigwait_nocancel = 422
SYS___semwait_signal_nocancel = 423
SYS___mac_mount = 424
SYS___mac_get_mount = 425
SYS___mac_getfsstat = 426
SYS_fsgetpath = 427
SYS_audit_session_self = 428
SYS_audit_session_join = 429
SYS_fileport_makeport = 430
SYS_fileport_makefd = 431
SYS_audit_session_port = 432
SYS_pid_suspend = 433
SYS_pid_resume = 434
SYS_pid_hibernate = 435
SYS_pid_shutdown_sockets = 436
SYS_kas_info = 439
SYS_memorystatus_control = 440
SYS_guarded_open_np = 441
SYS_guarded_close_np = 442
SYS_guarded_kqueue_np = 443
SYS_change_fdguard_np = 444
SYS_usrctl = 445
SYS_proc_rlimit_control = 446
SYS_connectx = 447
SYS_disconnectx = 448
SYS_peeloff = 449
SYS_socket_delegate = 450
SYS_telemetry = 451
SYS_proc_uuid_policy = 452
SYS_memorystatus_get_level = 453
SYS_system_override = 454
SYS_vfs_purge = 455
SYS_sfi_ctl = 456
SYS_sfi_pidctl = 457
SYS_coalition = 458
SYS_coalition_info = 459
SYS_necp_match_policy = 460
SYS_getattrlistbulk = 461
SYS_clonefileat = 462
SYS_openat = 463
SYS_openat_nocancel = 464
SYS_renameat = 465
SYS_faccessat = 466
SYS_fchmodat = 467
SYS_fchownat = 468
SYS_fstatat = 469
SYS_fstatat64 = 470
SYS_linkat = 471
SYS_unlinkat = 472
SYS_readlinkat = 473
SYS_symlinkat = 474
SYS_mkdirat = 475
SYS_getattrlistat = 476
SYS_proc_trace_log = 477
SYS_bsdthread_ctl = 478
SYS_openbyid_np = 479
SYS_recvmsg_x = 480
SYS_sendmsg_x = 481
SYS_thread_selfusage = 482
SYS_csrctl = 483
SYS_guarded_open_dprotected_np = 484
SYS_guarded_write_np = 485
SYS_guarded_pwrite_np = 486
SYS_guarded_writev_np = 487
SYS_renameatx_np = 488
SYS_mremap_encrypted = 489
SYS_netagent_trigger = 490
SYS_stack_snapshot_with_config = 491
SYS_microstackshot = 492
SYS_grab_pgo_data = 493
SYS_persona = 494
SYS_mach_eventlink_signal = 496
SYS_mach_eventlink_wait_until = 497
SYS_mach_eventlink_signal_wait_until = 498
SYS_work_interval_ctl = 499
SYS_getentropy = 500
SYS_necp_open = 501
SYS_necp_client_action = 502
SYS___nexus_open = 503
SYS___nexus_register = 504
SYS___nexus_deregister = 505
SYS___nexus_create = 506
SYS___nexus_destroy = 507
SYS___nexus_get_opt = 508
SYS___nexus_set_opt = 509
SYS___channel_open = 510
SYS___channel_get_info = 511
SYS___channel_sync = 512
SYS___channel_get_opt = 513
SYS___channel_set_opt = 514
SYS_ulock_wait = 515
SYS_ulock_wake = 516
SYS_fclonefileat = 517
SYS_fs_snapshot = 518
SYS_register_uexc_handler = 519
SYS_terminate_with_payload = 520
SYS_abort_with_payload = 521
SYS_necp_session_open = 522
SYS_necp_session_action = 523
SYS_setattrlistat = 524
SYS_net_qos_guideline = 525
SYS_fmount = 526
SYS_ntp_adjtime = 527
SYS_ntp_gettime = 528
SYS_os_fault_with_payload = 529
SYS_kqueue_workloop_ctl = 530
SYS___mach_bridge_remote_time = 531
SYS_coalition_ledger = 532
SYS_log_data = 533
SYS_memorystatus_available_memory = 534
SYS_objc_bp_assist_cfg_np = 535
SYS_shared_region_map_and_slide_2_np = 536
SYS_pivot_root = 537
SYS_task_inspect_for_pid = 538
SYS_task_read_for_pid = 539
SYS_preadv = 540
SYS_pwritev = 541
SYS_preadv_nocancel = 542
SYS_pwritev_nocancel = 543
SYS_ulock_wait2 = 544
SYS_proc_info_extended_id = 545
SYS_tracker_action = 546
SYS_debug_syscall_reject = 547
SYS_debug_syscall_reject_config = 548
SYS_graftdmg = 549
SYS_map_with_linking_np = 550
SYS_freadlink = 551
SYS_record_system_event = 552
SYS_mkfifoat = 553
SYS_mknodat = 554
SYS_ungraftdmg = 555
SYS_MAXSYSCALL = 556
SYS_invalid = 63
