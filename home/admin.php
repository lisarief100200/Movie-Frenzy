<?php
  $sql = $koneksi->query("SELECT COUNT(ID_CALON) as tot_calon  from tb_calon");
  while ($data= $sql->fetch_assoc()) {
    $calon=$data['tot_calon'];
  }

  $sql = $koneksi->query("SELECT COUNT(id_pengguna) as tot_pemilih  from tb_pengguna where level='Pemilih'");
  while ($data= $sql->fetch_assoc()) {
    $pemilih=$data['tot_pemilih'];
  }

  $sql = $koneksi->query("SELECT COUNT(id_pengguna) as sudah  from tb_pengguna where level='Pemilih' and status='0'");
  while ($data= $sql->fetch_assoc()) {
    $sudah=$data['sudah'];
  }

  $sql = $koneksi->query("SELECT COUNT(id_pengguna) as belum  from tb_pengguna where level='Pemilih' and status='1'");
  while ($data= $sql->fetch_assoc()) {
    $belum=$data['belum'];
  }

?>

<style>
* {
  box-sizing: border-box;
}

/* Create four equal columns that floats next to each other */
.column {
  float: left;
  width: 25%;
  padding: 10px;
}

</style>

<a><b>Prodi</b></a>
<div class="row">
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-info">
			<div class="inner">
				<h5>
					<?php echo $calon; ?>
				</h5>

				<p>Jumlah Kandidat</p>
			</div>
			<div class="icon">
				<i class="ion ion-stats-bars"></i>
			</div>
			<a href="" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-success">
			<div class="inner">
				<h5>
					<?php echo $pemilih; ?>
				</h5>

				<p>Jumlah Pemilih</p>
			</div>
			<div class="icon">
				<i class="ion ion-stats-bars"></i>
			</div>
			<a href="" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-warning">
			<div class="inner">
				<h5>
					<?php echo $sudah; ?>
				</h5>

				<p>Sudah Memilih</p>
			</div>
			<div class="icon">
				<i class="ion ion-person-add"></i>
			</div>
			<a href="#" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-danger">
			<div class="inner">
				<h5>
					<?php echo $belum; ?>
				</h5>

				<p>Belum Memlih</p>
			</div>
			<div class="icon">
				<i class="ion ion-person-add"></i>
			</div>
			<a href="#" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
</div>

<a><b>Fakultas</b></a>
<div class="row">
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-info">
			<div class="inner">
				<h5>
					<?php echo $calon; ?>
				</h5>

				<p>Jumlah Kandidat</p>
			</div>
			<div class="icon">
				<i class="ion ion-stats-bars"></i>
			</div>
			<a href="" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-success">
			<div class="inner">
				<h5>
					<?php echo $pemilih; ?>
				</h5>

				<p>Jumlah Pemilih</p>
			</div>
			<div class="icon">
				<i class="ion ion-stats-bars"></i>
			</div>
			<a href="" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-warning">
			<div class="inner">
				<h5>
					<?php echo $sudah; ?>
				</h5>

				<p>Sudah Memilih</p>
			</div>
			<div class="icon">
				<i class="ion ion-person-add"></i>
			</div>
			<a href="#" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-danger">
			<div class="inner">
				<h5>
					<?php echo $belum; ?>
				</h5>

				<p>Belum Memlih</p>
			</div>
			<div class="icon">
				<i class="ion ion-person-add"></i>
			</div>
			<a href="#" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
</div>

<a><b>Universitas</b></a>
<div class="row">
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-info">
			<div class="inner">
				<h5>
					<?php echo $calon; ?>
				</h5>

				<p>Jumlah Kandidat</p>
			</div>
			<div class="icon">
				<i class="ion ion-stats-bars"></i>
			</div>
			<a href="" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-success">
			<div class="inner">
				<h5>
					<?php echo $pemilih; ?>
				</h5>

				<p>Jumlah Pemilih</p>
			</div>
			<div class="icon">
				<i class="ion ion-stats-bars"></i>
			</div>
			<a href="" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-warning">
			<div class="inner">
				<h5>
					<?php echo $sudah; ?>
				</h5>

				<p>Sudah Memilih</p>
			</div>
			<div class="icon">
				<i class="ion ion-person-add"></i>
			</div>
			<a href="#" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
	<!-- ./col -->
	<div class="column">
		<!-- small box -->
		<div class="small-box bg-danger">
			<div class="inner">
				<h5>
					<?php echo $belum; ?>
				</h5>

				<p>Belum Memlih</p>
			</div>
			<div class="icon">
				<i class="ion ion-person-add"></i>
			</div>
			<a href="#" class="small-box-footer">Lihat Selengkapnya
				<i class="fas fa-arrow-circle-right"></i>
			</a>
		</div>
	</div>
</div>