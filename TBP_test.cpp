#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define p 4 /* star’s number +1 */
struct star {
    double m;
    double x;
    double y;
    double z;
    double px;
    double py;
    double pz;
    int flag;
};
void runge(struct star st[], struct star n_st[], double* Gp, float* dtp,
    double* sumxp, double* sumyp, double* sumzp, int* Kp);
main()
{
    FILE *fp[p], *fpd[p], *fl;
    char filename1[p][30], filename2[p][30], filenumber[30], filetail[30];
    float t, T, dt, d, L;
    int N, it, n, i, j, K;
    double G, l;
    double distance, distance_d;
    double m, x, y, z, px, py, pz, R, P;
    float dx, dy, dz, dpx, dpy, dpz;
    double sumx, sumy, sumz, sumxd, sumyd, sumzd;
    struct star st[p], std[p], n_st[p], n_std[p];
    G = 1.0;
    K = p - 1;
    printf("st[0].m = std[0].m = ");
    scanf("%lf", &st[0].m);
    std[0].m = st[0].m;
    st[0].x = 0.0;
    st[0].y = 0.0;
    st[0].z = 0.0;
    st[0].px = 0.0;
    st[0].py = 0.0;
    st[0].pz = 0.0;
    printf("0 <= st.m <= m\nm = ");
    scanf("%lf", &m);
    printf("-x <= st.x <= x\nx = ");
    scanf("%lf", &x);
    printf("-y <= st.y <= y\ny = ");
    scanf("%lf", &y);
    printf("-z <= st.z <= z\nz = ");
    scanf("%lf", &z);
    printf("-px <= st.px <= px\npx = ");
    scanf("%lf", &px);
    printf("-py <= st.py <= py\npy = ");
    scanf("%lf", &py);
    printf("-pz <= st.px <= pz\npz = ");
    scanf("%lf", &pz);
    printf("T = ");
    scanf("%f", &T);
    printf("dt = ");
    scanf("%f", &dt);
    printf("delta = ");
    scanf("%f", &d);
    n = 2000;
    printf("effective region = ");
    scanf("%f", &L);
    R = sqrt(x * x + y * y + z * z);
    P = sqrt(px * px + py * py + pz * pz);
    for (i = 1; i <= K; i++) {
        st[i].m = std[i].m = ((double)rand() / RAND_MAX) * m;
        do {
            st[i].x = ((double)rand() / RAND_MAX) * 2 * x - x;
            st[i].y = ((double)rand() / RAND_MAX) * 2 * y - y;
            st[i].z = ((double)rand() / RAND_MAX) * 2 * z - z;
        } while (sqrt(st[i].x * st[i].x + st[i].y * st[i].y + st[i].z * st[i].z) > R);
        do {
            st[i].px = ((double)rand() / RAND_MAX) * 2 * px - px;
            st[i].py = ((double)rand() / RAND_MAX) * 2 * py - py;
            st[i].pz = ((double)rand() / RAND_MAX) * 2 * pz - pz;
        } while (sqrt(st[i].px * st[i].px + st[i].py * st[i].py + st[i].pz * st[i].pz) > P);
        st[i].flag = 0;
    }
    dx = dy = dz = dpx = dpy = dpz = d;
    for (i = 0; i <= K; i++) {
        std[i].x = st[i].x + dx;
        std[i].y = st[i].y + dy;
        std[i].z = st[i].z + dz;
        std[i].px = st[i].px + dpx;
        std[i].py = st[i].py + dpy;
        std[i].pz = st[i].pz + dpz;
    }
    strcpy(filetail, "_1.dat");
    for (i = 0; i <= K; i++) {
        strcpy(filename1[i], "st");
        strcpy(filename2[i], "std");
        sprintf(filenumber, "%03d", i);
        strcat(filename1[i], filenumber);
        strcat(filename2[i], filenumber);
        strcat(filename1[i], filetail);
        strcat(filename2[i], filetail);
        fp[i] = fopen(filename1[i], "w");
        fpd[i] = fopen(filename2[i], "w");
    }
    fl = fopen("stl_1.dat", "w");
    N = T / dt;
    for (it = 0; it <= N; it = it + 1) {
        t = dt * it;
        l = 0.0;
        runge(st, n_st, &G, &dt, &sumx, &sumy, &sumz, &K);
        runge(std, n_std, &G, &dt, &sumxd, &sumyd, &sumzd, &K);
        for (i = 0; i <= K; i++) {
            st[i].x = n_st[i].x;
            std[i].x = n_std[i].x;
            st[i].y = n_st[i].y;
            std[i].y = n_std[i].y;
            st[i].z = n_st[i].z;
            std[i].z = n_std[i].z;
            st[i].px = n_st[i].px;
            std[i].px = n_std[i].px;
            st[i].py = n_st[i].py;
            std[i].py = n_std[i].py;
            st[i].pz = n_st[i].pz;
            std[i].pz = n_std[i].pz;
            distance = sqrt(st[i].x * st[i].x + st[i].y * st[i].y + st[i].z * st[i].z);
            distance_d = sqrt(std[i].x * std[i].x + std[i].y * std[i].y
                              + std[i].z * std[i].z);
            if ((distance > L || distance_d > L) && i != 0) {
                st[i].flag = 1;
            }
            if (st[i].flag == 0) {
                l += ((st[i].x - std[i].x) * (st[i].x - std[i].x))
                     + ((st[i].y - std[i].y) * (st[i].y - std[i].y))
                     + ((st[i].z - std[i].z) * (st[i].z - std[i].z))
                     + ((st[i].px - std[i].px) * (st[i].px - std[i].px))
                     + ((st[i].py - std[i].py) * (st[i].py - std[i].py))
                     + ((st[i].pz - std[i].pz) * (st[i].pz - std[i].pz));
            }
        }
        l = sqrt(l);
        if (it % n == 0 || it % n == 1) {
            for (i = 0; i <= K; i++) {
                if (st[i].flag == 0) {
                    fprintf(fp[i], "%e %le %le %le %le %le %le\n", t, st[i].x, st[i].y, st[i].z, st[i].px, st[i].py, st[i].pz);
                    fprintf(fpd[i], "%e %le %le %le %le %le %le\n", t, std[i].x, std[i].y, std[i].z,
                        std[i].px, std[i].py, std[i].pz);
                }
            }
            fprintf(fl, "%e %15.121f\n", t, l);
        }
    }
    for (i = 0; i <= K; i++) {
        fclose(fp[i]);
        fclose(fpd[i]);
    }
    fclose(fl);
}


void runge(struct star st[], struct star n_st[], double* Gp, float* dtp,
    double* sumxp, double* sumyp, double* sumzp, int* Kp)
{
    int i, j;
    struct star st_a[p], st_b[p], st_c[p], st_d[p], str[p];
    double r;
    for (i = 0; i <= *Kp; i++) {
        *sumxp = 0.0;
        *sumyp = 0.0;
        *sumzp = 0.0;
        if (st[i].flag == 0) {
            for (j = 0; j <= *Kp; j++) {
                if ((j != i) && (st[j].flag == 0)) {
                    r = (st[j].x - st[i].x) * (st[j].x - st[i].x)
                        + (st[j].y - st[i].y) * (st[j].y - st[i].y)
                        + (st[j].z - st[i].z) * (st[j].z - st[i].z);
                    *sumxp += (st[j].m * (st[j].x - st[i].x)) / (r * sqrt(r));
                    *sumyp += (st[j].m * (st[j].y - st[i].y)) / (r * sqrt(r));
                    *sumzp += (st[j].m * (st[j].z - st[i].z)) / (r * sqrt(r));
                }
            }
            st_a[i].x = (st[i].px / st[i].m) * (*dtp);
            st_a[i].y = (st[i].py / st[i].m) * (*dtp);
            st_a[i].z = (st[i].pz / st[i].m) * (*dtp);
            st_a[i].px = (*Gp) * (st[i].m) * (*sumxp) * (*dtp);
            st_a[i].py = (*Gp) * (st[i].m) * (*sumyp) * (*dtp);
            st_a[i].pz = (*Gp) * (st[i].m) * (*sumzp) * (*dtp);
        }
    }
    for (i = 0; i <= *Kp; i++) {
        if (st[i].flag == 0) {
            str[i].x = st[i].x + (st_a[i].x / 2);
            str[i].y = st[i].y + (st_a[i].y / 2);
            str[i].z = st[i].z + (st_a[i].z / 2);
            str[i].px = st[i].px + (st_a[i].px / 2);
            str[i].py = st[i].py + (st_a[i].py / 2);
            str[i].pz = st[i].pz + (st_a[i].pz / 2);
        }
    }
    for (i = 0; i <= *Kp; i++) {
        *sumxp = 0.0;
        *sumyp = 0.0;
        *sumzp = 0.0;
        if (st[i].flag == 0) {
            for (j = 0; j <= *Kp; j++) {
                if ((j != i) && (st[j].flag == 0)) {
                    r = (str[j].x - str[i].x) * (str[j].x - str[i].x)
                        + (str[j].y - str[i].y) * (str[j].y - str[i].y)
                        + (str[j].z - str[i].z) * (str[j].z - str[i].z);
                    *sumxp += (st[j].m * (str[j].x - str[i].x)) / (r * sqrt(r));
                    *sumyp += (st[j].m * (str[j].y - str[i].y)) / (r * sqrt(r));
                    *sumzp += (st[j].m * (str[j].z - str[i].z)) / (r * sqrt(r));
                }
            }
            st_b[i].x = (str[i].px / st[i].m) * (*dtp);
            st_b[i].y = (str[i].py / st[i].m) * (*dtp);
            st_b[i].z = (str[i].pz / st[i].m) * (*dtp);
            st_b[i].px = (*Gp) * (st[i].m) * (*sumxp) * (*dtp);
            st_b[i].py = (*Gp) * (st[i].m) * (*sumyp) * (*dtp);
            st_b[i].pz = (*Gp) * (st[i].m) * (*sumzp) * (*dtp);
        }
    }
    for (i = 0; i <= *Kp; i++) {
        if (st[i].flag == 0) {
            str[i].x = st[i].x + (st_b[i].x / 2);
            str[i].y = st[i].y + (st_b[i].y / 2);
            str[i].z = st[i].z + (st_b[i].z / 2);
            str[i].px = st[i].px + (st_b[i].px / 2);
            str[i].py = st[i].py + (st_b[i].py / 2);
            str[i].pz = st[i].pz + (st_b[i].pz / 2);
        }
    }
    for (i = 0; i <= *Kp; i++) {
        *sumxp = 0.0;
        *sumyp = 0.0;
        *sumzp = 0.0;
        if (st[i].flag == 0) {
            for (j = 0; j <= *Kp; j++) {
                if ((j != i) && (st[j].flag == 0)) {
                    r = (str[j].x - str[i].x) * (str[j].x - str[i].x)
                        + (str[j].y - str[i].y) * (str[j].y - str[i].y)
                        + (str[j].z - str[i].z) * (str[j].z - str[i].z);
                    *sumxp += (st[j].m * (str[j].x - str[i].x)) / (r * sqrt(r));
                    *sumyp += (st[j].m * (str[j].y - str[i].y)) / (r * sqrt(r));
                    *sumzp += (st[j].m * (str[j].z - str[i].z)) / (r * sqrt(r));
                }
            }
            st_c[i].x = (str[i].px / st[i].m) * (*dtp);
            st_c[i].y = (str[i].py / st[i].m) * (*dtp);
            st_c[i].z = (str[i].pz / st[i].m) * (*dtp);
            st_c[i].px = (*Gp) * (st[i].m) * (*sumxp) * (*dtp);
            st_c[i].py = (*Gp) * (st[i].m) * (*sumyp) * (*dtp);
            st_c[i].pz = (*Gp) * (st[i].m) * (*sumzp) * (*dtp);
        }
    }
    for (i = 0; i <= *Kp; i++) {
        if (st[i].flag == 0) {
            str[i].x = st[i].x + st_c[i].x;
            str[i].y = st[i].y + st_c[i].y;
            str[i].z = st[i].z + st_c[i].z;
            str[i].px = st[i].px + st_c[i].px;
            str[i].py = st[i].py + st_c[i].py;
            str[i].pz = st[i].pz + st_c[i].pz;
        }
    }
    for (i = 0; i <= *Kp; i++) {
        *sumxp = 0.0;
        *sumyp = 0.0;
        *sumzp = 0.0;
        if (st[i].flag == 0) {
            for (j = 0; j <= *Kp; j++) {
                if ((j != i) && (st[j].flag == 0)) {
                    r = (str[j].x - str[i].x) * (str[j].x - str[i].x)
                        + (str[j].y - str[i].y) * (str[j].y - str[i].y)
                        + (str[j].z - str[i].z) * (str[j].z - str[i].z);
                    *sumxp += (st[j].m * (str[j].x - str[i].x)) / (r * sqrt(r));
                    *sumyp += (st[j].m * (str[j].y - str[i].y)) / (r * sqrt(r));
                    *sumzp += (st[j].m * (str[j].z - str[i].z)) / (r * sqrt(r));
                }
            }
            st_d[i].x = (str[i].px / st[i].m) * (*dtp);
            st_d[i].y = (str[i].py / st[i].m) * (*dtp);
            st_d[i].z = (str[i].pz / st[i].m) * (*dtp);
            st_d[i].px = (*Gp) * (st[i].m) * (*sumxp) * (*dtp);
            st_d[i].py = (*Gp) * (st[i].m) * (*sumyp) * (*dtp);
            st_d[i].pz = (*Gp) * (st[i].m) * (*sumzp) * (*dtp);
        }
    }
    for (i = 0; i <= *Kp; i++) {
        if (st[i].flag == 0) {
            n_st[i].x = st[i].x + (st_a[i].x + 2 * st_b[i].x + 2 * st_c[i].x + st_d[i].x) / 6;
            n_st[i].y = st[i].y + (st_a[i].y + 2 * st_b[i].y + 2 * st_c[i].y + st_d[i].y) / 6;
            n_st[i].z = st[i].z + (st_a[i].z + 2 * st_b[i].z + 2 * st_c[i].z + st_d[i].z) / 6;
            n_st[i].px = st[i].px + (st_a[i].px + 2 * st_b[i].px + 2 * st_c[i].px + st_d[i].px) / 6;
            n_st[i].py = st[i].py + (st_a[i].py + 2 * st_b[i].py + 2 * st_c[i].py + st_d[i].py) / 6;
            n_st[i].pz = st[i].pz + (st_a[i].pz + 2 * st_b[i].pz + 2 * st_c[i].pz + st_d[i].pz) / 6;
        }
    }
}
