# -*- coding: utf-8 -*-

from odoo import models, fields, api

class siswaAddonsSekolah(models.Model):
    _name = 'addons_sekolah.siswa'
    _description = 'Addons Sekolah : Siswa'

    nis = fields.Char('NIS')
    nm_siswa = fields.Char('Nama Siswa')
    jns_kelamin = fields.Selection([
        ('laki-laki', 'Laki-Laki'),
        ('perempuan', 'Perempuan')
    ], string='Jenis Kelamin')
    tgl_lahir = fields.Date('Tanggal Lahir')
    agama = fields.Char('Agama')
    nm_ayah = fields.Char('Nama Ayah')
    nm_ibu = fields.Char('Nama Ibu')
    usia = fields.Integer('Usia')
    alamat = fields.Text('Alamat')

    name = fields.Char('Nama Siswa', compute='_compute_nama_siswa', store=True)

    @api.depends('nm_siswa')
    def _compute_nama_siswa(self):
        for record in self:
            record.name = record.nm_siswa if record.nm_siswa else 'Nama Siswa Tidak Tersedia'

    siswa_id = fields.Many2one('addons_sekolah.siswa', 'Siswa')

class guruAddonsSekolah(models.Model):
    _name = 'addons_sekolah.guru'
    _description = 'Addons Sekolah : Guru'

    nip = fields.Char('NIP')
    nm_guru = fields.Char('Nama Guru')
    jns_kelamin = fields.Selection([
        ('laki-laki', 'Laki-Laki'),
        ('perempuan', 'Perempuan')
    ], string='Jenis Kelamin')
    usia = fields.Integer('Usia')
    no_telp = fields.Char('No Telepon')
    alamat = fields.Text('Alamat')
    mapel_id = fields.Many2one('addons_sekolah.matapelajaran', string='Mata Pelajaran')

    name = fields.Char('Nama Guru', compute='_compute_nama_guru', store=True)

    @api.depends('nm_guru')
    def _compute_nama_guru(self):
        for record in self:
            record.name = record.nm_guru if record.nm_guru else 'Nama Guru Tidak Tersedia'
    # mata pelajaran
    
class kelasAddonsSekolah(models.Model):
    _name = 'addons_sekolah.kelas'
    _description = 'Addons Sekolah : Kelas'

    nm_kelas = fields.Char('Nama Kelas')
    siswa_ids = fields.One2many('addons_sekolah.siswa', 'siswa_id', string='Siswa')
    wali_id = fields.Many2one('addons_sekolah.guru', string='Wali Kelas')

    name = fields.Char('Nama Kelas', compute='_compute_nama_kelas', store=True)

    @api.depends('nm_kelas')
    def _compute_nama_kelas(self):
        for record in self:
            record.name = record.nm_kelas if record.nm_kelas else 'Nama Kelas Tidak Tersedia'

    # nama siswa
    # wali kelas

class mapelAddonsSekolah(models.Model):
    _name = 'addons_sekolah.matapelajaran'
    _description = 'Addons Sekolah : Mata Pelajaran'

    nm_matapelajaran = fields.Char('Nama Mata Pelajaran')
    jurusan = fields.Char('Jurusan')

    name = fields.Char('Nama Mata Pelajaran', compute='_compute_nama_matapelajaran', store=True)

    @api.depends('nm_matapelajaran')
    def _compute_nama_matapelajaran(self):
        for record in self:
            record.name = record.nm_matapelajaran if record.nm_matapelajaran else 'Nama Mata Pelajaran Tidak Tersedia'

class jadwalAddonsSekolah(models.Model):
    _name = 'addons_sekolah.jadwal'
    _description = 'Addons Sekolah : Jadwal'

    hari = fields.Char('Hari')
    jam = fields.Float(string='Jam')
    kelas_id = fields.Many2one('addons_sekolah.kelas', string='Kelas')
    mapel_id = fields.Many2one('addons_sekolah.matapelajaran', string='Mata Pelajaran')
    # kelas
    # matapelajaran
    
    

    
