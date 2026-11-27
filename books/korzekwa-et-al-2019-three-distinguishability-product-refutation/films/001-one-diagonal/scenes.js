'use strict';

const heading = (title, subtitle) => {
  txt(title, W / 2, 140, {size: 58, align: 'center', c: C.white});
  txt(subtitle, W / 2, 206, {size: 28, align: 'center', c: C.cyan});
};

SCENES.lights = scene => {
  heading('One diagonal, three states', 'WHAT DOES THE ORIGINAL MEASUREMENT SEE?');
  const probabilities = ['1/6', '1/4', '7/24', '7/24'];
  probabilities.forEach((value, index) => {
    const x = W / 2 - 548 + index * 280;
    const visible = at(scene, 1, 0.45, 0.18 * index);
    panel(x, 345, 255, 260, visible, C.cyan, `LAMP ${index + 1}`);
    txt(value, x + 127, 500, {size: 58, align: 'center', fam: F.mono, c: C.white, a: visible});
  });
};

SCENES.phases = scene => {
  heading('Keep the magnitudes; vary the phases', 'THREE VECTORS WITH THE SAME SQUARED MAGNITUDES');
  const rows = [['1', '1', '1', '1'], ['1', 'ω', 'v', 'w'], ['1', 'ω', 'w', 'v']];
  rows.forEach((row, index) => {
    const y = 328 + index * 145;
    const visible = at(scene, Math.min(index, 1), 0.55, index * 0.24);
    panel(W / 2 - 530, y - 60, 1060, 118, visible, index === 2 ? C.now : C.cyan, `VECTOR ${index + 1}`);
    row.forEach((phase, column) => {
      txt(phase, W / 2 - 246 + column * 164, y + 13, {size: 54, align: 'center', c: column > 1 && index > 0 ? C.now : C.white, a: visible});
    });
  });
  txt('All three pairwise inner products = 0', W / 2, 767, {size: 42, align: 'center', c: C.white, a: at(scene, 2, 0.55)});
};

SCENES.pairing = scene => {
  heading('Which opposite products match?', 'RESIDUAL WEIGHTS: 1/2   1/4   1/8   1/8');
  const top = ['1/2 × 1/4', '1/2 × 1/8', '1/2 × 1/8'];
  const bottom = ['1/8 × 1/8', '1/4 × 1/8', '1/4 × 1/8'];
  const gaps = ['7/64', '1/32', '1/32'];
  top.forEach((value, index) => {
    const x = W / 2 - 698 + index * 475;
    const visible = at(scene, 1, 0.55, index * 0.17);
    panel(x, 320, 445, 380, visible, C.cyan, `PAIRING ${index + 1}`);
    txt(value, x + 222, 438, {size: 44, align: 'center', fam: F.mono, c: C.white, a: visible});
    txt(`− ${bottom[index]}`, x + 222, 515, {size: 44, align: 'center', fam: F.mono, c: C.white, a: visible});
    txt(`${gaps[index]} ≠ 0`, x + 222, 625, {size: 52, align: 'center', c: C.now, a: at(scene, 2, 0.48, index * 0.28)});
  });
};

SCENES.scope = scene => {
  heading('Attainable, but not a product', 'A COUNTEREXAMPLE TO NECESSITY');
  const visible = at(scene, 0, 0.55);
  panel(W / 2 - 610, 300, 1220, 245, visible, C.now, 'TWO CHECKS, DIFFERENT CONCLUSIONS');
  txt('Orthogonal witnesses: yes', W / 2, 405, {size: 46, align: 'center', c: C.white, a: visible});
  txt('Product form in any ordering: no', W / 2, 490, {size: 46, align: 'center', c: C.now, a: visible});
  const credit = at(scene, 1, 0.55);
  txt('Counterexamples: Haobo Ma and Wenlin Zhang', W / 2, 660, {size: 33, align: 'center', c: C.white, a: credit});
  txt('Earlier centre-to-edge construction: Korzekwa et al.', W / 2, 720, {size: 33, align: 'center', c: C.white, a: credit});
};
