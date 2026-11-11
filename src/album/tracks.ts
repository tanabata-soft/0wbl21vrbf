// 曲目と解説（この作品のデータ）。src は歌詞データ（src/album/sync.ts）のキー。
// 並びが曲順。シングルでは1曲目が表題曲、2曲目がカップリング（docs/SINGLE.md）。
// 曲順は推奨案の仮置き（確認ポイント①）。time はトリム後の実測（floor）。
import type { TrackMeta } from '../logic';

export const TRACKS: TrackMeta[] = [
  { src: '黒い画面の喝采', title: '黒い画面の喝采', genre: '90s Japanese Funk Rock', time: '2:48', note: '90年代ファンク・ロックの応援歌。真っ黒な画面とにらめっこしてバグを探す、地味と言われた仕事を「世界を救う仕事だぜ」と胸を張る。金のマイクの喝采。品質と変革を掲げ、現場から「ド派手に行こうぜ」と笑い飛ばす、表題曲。' },
  { src: '時代を動かせ', title: '時代を動かせ', genre: 'Electronic Hip-Hop', time: '2:31', note: 'エレクトロニック・ヒップホップの応援歌。画面の向こうに広がる世界で、すべてを塗り替える。テストの砦から始まったストーリーがITの頂点を掴み、「We keep the SHIFT!」と進化を止めない。時代の歯車を高速で回す、カップリング。' },
];
